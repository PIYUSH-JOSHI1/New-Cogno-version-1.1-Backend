"""
Cogno Solution - Email Templates
================================
Beautiful, responsive HTML email templates for different application scenarios.
"""

def get_base_template(content: str, title: str = "Cogno Solution Notification") -> str:
    """Standard responsive wrapper for all emails."""
    return f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>{title}</title>
        <style>
            body {{ font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; line-height: 1.6; color: #333; margin: 0; padding: 0; background-color: #f4f7f9; }}
            .container {{ max-width: 600px; margin: 20px auto; background: #ffffff; border-radius: 12px; overflow: hidden; box-shadow: 0 4px 15px rgba(0,0,0,0.05); }}
            .header {{ background: linear-gradient(135deg, #3b82f6 0%, #2563eb 100%); padding: 30px; text-align: center; color: white; }}
            .header h1 {{ margin: 0; font-size: 24px; font-weight: 700; letter-spacing: 0.5px; }}
            .logo {{ width: 50px; height: 50px; margin-bottom: 10px; }}
            .content {{ padding: 40px; }}
            .footer {{ background: #f8fafc; padding: 20px; text-align: center; font-size: 12px; color: #64748b; border-top: 1px solid #e2e8f0; }}
            .btn {{ display: inline-block; padding: 12px 24px; background-color: #3b82f6; color: white !important; text-decoration: none; border-radius: 6px; font-weight: 600; margin-top: 20px; }}
            .highlight {{ color: #3b82f6; font-weight: 700; }}
            .card {{ background: #f1f5f9; border-radius: 8px; padding: 20px; margin: 20px 0; }}
            .footer-links a {{ color: #3b82f6; text-decoration: none; margin: 0 10px; }}
        </style>
    </head>
    <body>
        <div class="container">
            <div class="header">
                <img src="https://uebxekueqiqucplaihuz.supabase.co/storage/v1/object/public/assets/logo-white.png" alt="Cogno Logo" class="logo" onerror="this.style.display='none'">
                <h1>Cogno Solution</h1>
            </div>
            <div class="content">
                {content}
            </div>
            <div class="footer">
                <p>&copy; 2026 Cogno Solution. Empowering minds, one step at a time.</p>
                <div class="footer-links">
                    <a href="#">Privacy Policy</a>
                    <a href="#">Support</a>
                </div>
            </div>
        </div>
    </body>
    </html>
    """

def get_report_email(user_name: str, report_summary: dict) -> str:
    """Template for progress report notification."""
    content = f"""
    <h2>Hi {user_name},</h2>
    <p>Your latest <span class="highlight">Progress Report</span> is ready! Here's a snapshot of your recent learning journey:</p>
    
    <div class="card">
        <p><strong>Total Sessions:</strong> {report_summary.get('total_sessions', 0)}</p>
        <p><strong>Practice Time:</strong> {report_summary.get('total_time_minutes', 0)} mins</p>
        <p><strong>Average Score:</strong> {report_summary.get('average_score', 0)}%</p>
        <p><strong>Improvement:</strong> <span style="color: #10b981;">+{report_summary.get('improvement', 0)}%</span></p>
    </div>
    
    <p>Consistency is the key to mastery. You're doing a great job staying on track!</p>
    
    <a href="https://cognosolution.com/dashboard" class="btn">View Full Detailed Report</a>
    
    <p style="margin-top: 30px;">Keep up the fantastic work!</p>
    <p>Best regards,<br>The Cogno Team</p>
    """
    return get_base_template(content, "Your Progress Report is Ready")

def get_appointment_reminder_email(user_name: str, doctor_name: str, date_time: str) -> str:
    """Template for consultation reminders."""
    content = f"""
    <h2>Appointment Reminder</h2>
    <p>Hello {user_name},</p>
    <p>This is a friendly reminder that you have a scheduled consultation tomorrow:</p>
    
    <div class="card" style="border-left: 4px solid #3b82f6;">
        <p><strong>Specialist:</strong> Dr. {doctor_name}</p>
        <p><strong>Date & Time:</strong> {date_time}</p>
        <p><strong>Mode:</strong> Secure Video Call</p>
    </div>
    
    <p>Please make sure you have a stable internet connection and are in a quiet environment for the session.</p>
    
    <a href="https://cognosolution.com/consultations" class="btn">Join Session Room</a>
    
    <p style="margin-top: 30px; font-size: 0.9rem; color: #64748b;">If you need to reschedule, please notify us at least 12 hours in advance.</p>
    """
    return get_base_template(content, "Appointment Reminder: Tomorrow")

def get_achievement_email(user_name: str, achievement_title: str, achievement_desc: str) -> str:
    """Template for achievement milestones."""
    content = f"""
    <div style="text-align: center;">
        <h1 style="color: #f59e0b; font-size: 40px; margin-bottom: 10px;">🏆</h1>
        <h2 style="color: #f59e0b;">New Achievement Unlocked!</h2>
    </div>
    
    <p>Boom! Way to go, <span class="highlight">{user_name}</span>!</p>
    <p>You've just earned the <strong>"{achievement_title}"</strong> milestone.</p>
    
    <div class="card" style="text-align: center; background: #fffcf0; border: 1px solid #fef3c7;">
        <h3 style="color: #d97706; margin-bottom: 5px;">{achievement_title}</h3>
        <p style="font-style: italic; color: #92400e;">{achievement_desc}</p>
    </div>
    
    <p>Every milestone you hit brings you closer to your goals. Share your progress and celebrate your success!</p>
    
    <a href="https://cognosolution.com/achievements" class="btn" style="background-color: #f59e0b;">See Your Trophy Room</a>
    
    <p style="margin-top: 30px;">Proud of you,<br>The Cogno Team</p>
    """
    return get_base_template(content, f"🏆 Congratulations! You earned: {achievement_title}")

def get_login_email(user_name: str, device_info: str = "A new device") -> str:
    """Template for login notifications."""
    content = f"""
    <h2>Hello {user_name},</h2>
    <p>You have successfully logged into your <span class="highlight">Cogno Solution</span> account.</p>
    
    <div class="card">
        <p><strong>Time:</strong> {datetime.utcnow().strftime('%B %d, %Y at %H:%M UTC')}</p>
        <p><strong>Device/Browser:</strong> {device_info}</p>
    </div>
    
    <p>If this was you, you can safely disregard this email. We just wanted to make sure your account is secure.</p>
    
    <p>Ready to continue your learning journey?</p>
    
    <a href="https://cognosolution.com/dashboard" class="btn">Go to Dashboard</a>
    
    <p style="margin-top: 30px; font-size: 0.8rem; color: #94a3b8;">If you did not authorize this login, please change your password immediately or contact our support team.</p>
    """
    return get_base_template(content, "Login Notification")
