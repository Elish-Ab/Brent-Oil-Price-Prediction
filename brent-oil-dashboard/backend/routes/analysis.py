from flask import Blueprint, jsonify
import pandas as pd

analysis_bp = Blueprint('analysis', __name__)

# Load Brent Oil Price Data
df = pd.read_csv('/home/elisha-a/week10/brent-oil-dashboard/backend/data/BrentOilPrices.csv')
@analysis_bp.route('/api/historical', methods=['GET'])
def historical_data():
    return jsonify(df.to_dict(orient="records"))

