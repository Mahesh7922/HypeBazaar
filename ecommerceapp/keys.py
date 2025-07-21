# Import environment variables
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Paytm settings (commented out but included for reference)
# PAYTM_MERCHANT_ID = os.environ.get("PAYTM_MERCHANT_ID")
# PAYTM_SECRET_KEY = os.environ.get("PAYTM_SECRET_KEY")
# MID = os.environ.get("PAYTM_MID")
# MK = os.environ.get("PAYTM_MK")

# PhonePe settings (commented out but included for reference)
# PHONEPE_MERCHANT_ID = os.environ.get("PHONEPE_MERCHANT_ID")
# PHONEPE_SALT_KEY = os.environ.get("PHONEPE_SALT_KEY")
# PHONEPE_BASE_URL = os.environ.get("PHONEPE_BASE_URL")  # Use production URL for live

# Razorpay settings
RAZORPAY_KEY_ID = os.environ.get("RAZORPAY_KEY_ID")
RAZORPAY_KEY_SECRET = os.environ.get("RAZORPAY_KEY_SECRET")
