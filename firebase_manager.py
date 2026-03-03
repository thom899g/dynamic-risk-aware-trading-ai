"""
Firebase state management for trading AI.
Handles all real-time data persistence and retrieval.
"""
import logging
from typing import Dict, Any, Optional, List
import datetime
from google.cloud import firestore
import firebase_admin
from firebase_admin import credentials, firestore
from google.cloud.firestore_v1.base_query import FieldFilter

class FirebaseManager:
    """Manages all Firebase Firestore operations for trading system"""
    
    def __init__(self, service_account_key_path: str =