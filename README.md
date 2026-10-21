# Curry Nation — Hostinger Node.js deployment

This repository is arranged so the **repository root is the Node.js application root**. Hostinger starts `server.js`; Express serves the finished website from `public/`, while `/api/contact` sends the contact form through SMTP.

## Folder structure

```text
.
├── package.json          # Hostinger installs dependencies and runs npm start
├── server.js             # Node server + contact form API
├── .env.example          # Example settings only; never put real passwords here
├── public/               # Website document root served by Express
│   ├── index.html
│   ├── contact.html
│   ├── about.html
│   ├── assets/            # All site images/icons, preserving their relative paths
│   └── ...other HTML pages
└── source/                # Original Python source/build files retained for reference
```

All original generated HTML pages and the entire `site/assets/` folder have been moved together under `public/`. Existing paths such as `assets/cn/about-gallery2.jpg` therefore resolve relative to each HTML page, without a Hostinger `public_html` upload step. Do not move `assets/` out of `public/`.

## Deploy from GitHub to Hostinger

1. Push the **contents of this folder** to the root of your GitHub repository (so `package.json` and `server.js` are at repository root).
2. In Hostinger hPanel, open **Websites → Add Website / Node.js** (wording varies by plan) and connect the GitHub repository.
3. Set the application root to the repository root, startup command to `npm start` if asked, and use a supported Node.js version (20 or newer).
4. Deploy/redeploy. Hostinger should install dependencies from `package.json`; do not point the application root at `public/`.
5. Add the environment variables below in the Node.js app settings, then restart/redeploy the app.
6. Connect `currynation.in` to this Node.js application using Hostinger's domain/Node.js app settings. You should not need to manually upload files into `public_html`.

Hostinger's available Node.js deployment options depend on the hosting plan. If your hPanel does not show a Node.js application option, the plan may not support this deployment method.

## Contact form email (Google Workspace)

Add these environment variables in Hostinger's application settings. Do not commit real credentials to GitHub.

| Variable | Value |
|---|---|
| `SMTP_HOST` | `smtp.gmail.com` |
| `SMTP_PORT` | `465` |
| `SMTP_USER` | `challengeus@currynation.in` |
| `SMTP_PASS` | A Google Workspace App Password for that mailbox |
| `MAIL_TO` | `challengeus@currynation.in` |
| `MAIL_FROM` | `challengeus@currynation.in` |
| `NODE_ENV` | `production` |

If Google Workspace 2-Step Verification is enabled and your account permits App Passwords, create an app password and use it as `SMTP_PASS`. Do not use your normal Google password. If your Workspace administrator disables app passwords or SMTP AUTH, use an approved alternative mail provider/API. Keep credentials only in Hostinger environment variables.

The contact form posts to `/api/contact`; successful submissions are emailed to `challengeus@currynation.in`. The visitor's email is used as `Reply-To`, so replies go back to the person who submitted the form.

## Test after deployment

1. Open `https://currynation.in/` and check the home page.
2. Open `https://currynation.in/about.html`, `/work.html`, `/resources.html`, and `/contact.html`; check that photos, logos, and icons appear.
3. Open `https://currynation.in/health`; it should say the Node app is running.
4. Submit the contact form with a real email address and verify delivery to `challengeus@currynation.in`.
5. If the form fails, inspect Hostinger application logs and verify the SMTP environment variables and Google Workspace SMTP access.

## Important

- `.env.example` is a template, not a live credentials file. Never upload your real SMTP password.
- Existing content and page filenames have been preserved to avoid breaking internal links.
- The `source/` folder preserves the original build inputs, but Hostinger serves the already-generated HTML from `public/`; Python is not required to run the deployed site.
