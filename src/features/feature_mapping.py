DATASET_KEYS = {"student", "mental"}

TARGET_MAP = {
    "student" : "performance_index",
    "mental" : "mood_score"
}

FEATURE_MAP = {
    "student": {
        "sleep_hours": "sleep_hours",
        "screen_time_hours": "screen_time_hours",
        "exercise_minutes": None,              # not available in student dataset
        "caffeine_intake": "caffeine_intake",
        "stress_level": "stress_level",

        "study_hours": "study_hours",
        "attendance_rate": "attendance_rate",
        "diet_quality": None,
        "interruptions": None,
        "daily_pending_tasks": None,
        "social_hours": None,
        "weather": None,
    },
    "mental": {
        "sleep_hours": "sleep_hours",
        "screen_time_hours": "screen_time",    # different name in mental dataset
        "exercise_minutes": "exercise_minutes",
        "caffeine_intake": "coffee_cups",      # different name in mental dataset
        "stress_level": "stress_level",

        "study_hours": None,
        "attendance_rate": None,
        "diet_quality": "diet_quality",
        "interruptions": "interruptions",
        "daily_pending_tasks": "daily_pending_tasks",
        "social_hours": "social_hours",
        "weather": "weather",
    },
}