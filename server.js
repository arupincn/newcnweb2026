const express = require('express');
const path = require('path');
const multer = require('multer');
const rateLimit = require('express-rate-limit');
const nodemailer = require('nodemailer');

const app = express();
const PORT = process.env.PORT || 3000;
const PUBLIC_DIR = path.join(__dirname, 'public');

app.disable('x-powered-by');
app.use(express.urlencoded({ extended: false, limit: '20kb' }));
app.use(express.json({ limit: '20kb' }));

const contactLimiter = rateLimit({
  windowMs: 15 * 60 * 1000,
  limit: 5,
  standardHeaders: 'draft-7',
  legacyHeaders: false,
  message: { error: 'Too many messages submitted. Please wait a little and try again.' }
});
const parseForm = multer({ limits: { fieldSize: 10 * 1024, fields: 10 } }).none();

app.get('/health', (_req, res) => res.status(200).send('Curry Nation Node app is running.'));

app.post('/api/contact', contactLimiter, parseForm, async (req, res) => {
  try {
    const { name = '', phone = '', email = '', message = '', website = '' } = req.body || {};

    // Honeypot: silently accept bot submissions without sending email.
    if (String(website).trim()) return res.status(200).json({ ok: true });

    const clean = value => String(value || '').trim();
    const senderName = clean(name).slice(0, 150);
    const senderPhone = clean(phone).slice(0, 80);
    const senderEmail = clean(email).slice(0, 254);
    const senderMessage = clean(message).slice(0, 5000);

    if (!senderName || !senderPhone || !senderEmail) {
      return res.status(400).json({ error: 'Please provide your name, phone number, and email address.' });
    }
    if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(senderEmail)) {
      return res.status(400).json({ error: 'Please enter a valid email address.' });
    }

    const required = ['SMTP_HOST', 'SMTP_PORT', 'SMTP_USER', 'SMTP_PASS', 'MAIL_TO'];
    const missing = required.filter(key => !process.env[key]);
    if (missing.length) {
      console.error('Contact email configuration is missing:', missing.join(', '));
      return res.status(503).json({ error: 'The contact form email service is not configured yet. Please email challengeus@currynation.in directly.' });
    }

    const port = Number(process.env.SMTP_PORT);
    const transporter = nodemailer.createTransport({
      host: process.env.SMTP_HOST,
      port,
      secure: port === 465,
      auth: { user: process.env.SMTP_USER, pass: process.env.SMTP_PASS }
    });

    await transporter.sendMail({
      from: process.env.MAIL_FROM || process.env.SMTP_USER,
      to: process.env.MAIL_TO,
      replyTo: { name: senderName, address: senderEmail },
      subject: `Curry Nation website enquiry — ${senderName}`,
      text: `New enquiry from currynation.in\n\nName: ${senderName}\nPhone: ${senderPhone}\nEmail: ${senderEmail}\n\nMessage:\n${senderMessage || '(No message provided)'}`,
      html: `<h2>New Curry Nation website enquiry</h2>
        <p><strong>Name:</strong> ${escapeHtml(senderName)}</p>
        <p><strong>Phone:</strong> ${escapeHtml(senderPhone)}</p>
        <p><strong>Email:</strong> ${escapeHtml(senderEmail)}</p>
        <p><strong>Message:</strong><br>${escapeHtml(senderMessage || '(No message provided)').replace(/\n/g, '<br>')}</p>`
    });

    return res.status(200).json({ ok: true });
  } catch (error) {
    console.error('Contact form failed:', error && error.message ? error.message : error);
    return res.status(500).json({ error: 'We could not send your message right now. Please try again later or email challengeus@currynation.in.' });
  }
});

function escapeHtml(value) {
  return String(value).replace(/[&<>"']/g, char => ({
    '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;'
  }[char]));
}

app.use(express.static(PUBLIC_DIR, {
  extensions: ['html'],
  maxAge: process.env.NODE_ENV === 'production' ? '1h' : 0
}));
app.get('*', (req, res, next) => {
  // Serve an exact static file if present; otherwise show the homepage.
  if (req.path === '/') return res.sendFile(path.join(PUBLIC_DIR, 'index.html'));
  next();
});
app.use((req, res) => res.status(404).sendFile(path.join(PUBLIC_DIR, '404.html'), err => {
  if (err) res.status(404).send('Page not found');
}));

app.listen(PORT, '0.0.0.0', () => console.log(`Curry Nation server listening on port ${PORT}`));
