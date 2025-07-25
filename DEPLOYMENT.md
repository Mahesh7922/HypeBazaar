# Django Ecommerce Deployment Guide

This guide will help you deploy your Django ecommerce project to Render.com with a free PostgreSQL database from Neon.

## 🗄️ Setting up Free PostgreSQL Database with Neon

### Step 1: Create a Neon Account

1. Go to [Neon.tech](https://neon.tech) and sign up for a free account
2. Click "Create Project" to create a new PostgreSQL database
3. Choose your preferred region (closest to your users for better performance)

### Step 2: Get Database Connection Details

1. After creating your project, go to the **Dashboard**
2. Click on **"Connect"** to get your connection string
3. Copy the connection string - it should look like:
   ```
   postgresql://username:password@hostname.neon.tech/dbname?sslmode=require
   ```
4. Keep this safe - you'll need it for deployment

### Step 3: Set up Database Schema

1. In the Neon console, go to **SQL Editor**
2. Run your Django migrations by connecting via your local environment first:
   ```bash
   # Set your DATABASE_URL temporarily
   export DATABASE_URL="your-neon-connection-string"
   python manage.py migrate
   ```

## 🚀 Deploying to Render.com

### Step 1: Prepare Your Repository

1. Make sure your code is in a GitHub repository
2. Ensure all changes are committed and pushed:
   ```bash
   git add .
   git commit -m "Prepare for deployment"
   git push origin main
   ```

### Step 2: Create Render Account

1. Go to [Render.com](https://render.com) and sign up
2. Connect your GitHub account to Render

### Step 3: Create Web Service

1. Click **"New +"** → **"Web Service"**
2. Connect your GitHub repository
3. Configure the service:
   - **Name**: Your app name (e.g., `my-ecommerce-app`)
   - **Region**: Choose closest to your users
   - **Branch**: `main`
   - **Runtime**: `Python 3`
   - **Build Command**: `./build.sh`
   - **Start Command**: `gunicorn ecommerce.wsgi:application`

### Step 4: Set Environment Variables

In the Render dashboard, add these environment variables:

```bash
# Required Variables
SECRET_KEY=your-django-secret-key-here
DEBUG=False
ALLOWED_HOSTS=your-app-name.onrender.com
DATABASE_URL=your-neon-connection-string

# Email Configuration (optional)
EMAIL_HOST=smtp.gmail.com
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-app-password
EMAIL_PORT=587
EMAIL_USE_TLS=True
```

**Important Notes:**
- Generate a strong `SECRET_KEY` (you can use [Django Secret Key Generator](https://djecrety.ir/))
- Replace `your-app-name` in `ALLOWED_HOSTS` with your actual Render app name
- Use the exact `DATABASE_URL` from your Neon dashboard

### Step 5: Deploy

1. Click **"Create Web Service"**
2. Render will automatically build and deploy your application
3. The build process will:
   - Install dependencies
   - Collect static files
   - Run database migrations

## 🔧 Alternative Free Database Options

If you prefer other providers, here are alternatives:

### 1. Supabase (PostgreSQL)
- Free tier: 500MB database, 2 projects
- Sign up at [supabase.com](https://supabase.com)
- Get connection string from Project Settings → Database

### 2. Railway (PostgreSQL)
- Free tier: $5 credit monthly
- Sign up at [railway.app](https://railway.app)
- Create PostgreSQL service and get connection URL

### 3. Aiven (PostgreSQL)
- Free tier: 1GB RAM, 5GB storage
- Sign up at [aiven.io](https://aiven.io)
- Create PostgreSQL service

## 🔍 Troubleshooting

### Common Issues:

1. **Build fails**: Check your `requirements.txt` for syntax errors
2. **Database connection fails**: Verify your `DATABASE_URL` is correct
3. **Static files not loading**: Ensure `STATIC_ROOT` is configured correctly
4. **Migration errors**: Make sure your database is accessible

### Debugging Steps:

1. Check Render logs in the dashboard
2. Verify environment variables are set correctly
3. Test database connection locally with the same `DATABASE_URL`
4. Make sure your `ALLOWED_HOSTS` includes your Render domain

## 📝 Post-Deployment Checklist

- [ ] Application loads successfully
- [ ] Database migrations ran successfully
- [ ] Static files are serving correctly
- [ ] Admin panel is accessible
- [ ] Email functionality works (if configured)
- [ ] All app features work as expected

## 🔒 Security Notes

- Never commit sensitive data like secret keys to your repository
- Use environment variables for all sensitive configuration
- Keep your Django and package versions updated
- Consider setting up proper error monitoring

## 🆘 Getting Help

If you encounter issues:

1. Check Render deployment logs
2. Review Neon database logs
3. Ensure all environment variables are properly set
4. Verify your database connection string is correct

Your Django ecommerce app should now be live and accessible via your Render.com URL!