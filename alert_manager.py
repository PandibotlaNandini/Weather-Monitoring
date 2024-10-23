def check_alert_conditions(data, threshold=35, consecutive_alerts=2):
    static previous_alert_count = 0

    if data["temperature"] > threshold:
        previous_alert_count += 1
    else:
        previous_alert_count = 0

    if previous_alert_count >= consecutive_alerts:
        print(f"ALERT: {data['city']} temperature exceeded {threshold}°C for consecutive updates.")
        previous_alert_count = 0
