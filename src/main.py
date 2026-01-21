from src.data.loaders import DatasetLoader
from src.features.feature_mapping import FEATURE_MAP, TARGET_MAP
from src.features.feature_engineering import standardize_df
from src.data.preprocessors import split_features_target

#prints basic info about the datasets 
def inspect_df(name: str, df):
    print(f"\n===== {name} =====")
    print("Shape:", df.shape)

    print("\nColumns:")
    print(df.columns.tolist())

    print("\nInfo (types + missing values):")
    df.info()


#validating the mapping for the data sets - targets and features 
def validate_mapping(dataset_name: str, df):
    print(f"Validating for: {dataset_name}") 

    target_col = TARGET_MAP[dataset_name] 
    if target_col not in df.columns: 
        raise ValueError(f"Target column '{target_col}' not found in {dataset_name} ")
    
    missing = [] 

    for canonical, actual in FEATURE_MAP[dataset_name].items():
        if actual is None:
            continue 
        if actual not in df.columns:
            missing.append((canonical, actual))
    
    if missing:
        print("❌ Missing mapped columns:")
        for canonical, actual in missing:
            print(f"  - canonical '{canonical}' -> expected '{actual}' (not found)")
    else:
        print("✅ All mapped columns found.")





def main():
    student_loader = DatasetLoader("data/raw/student_learning_trajectory.csv")
    mental_loader = DatasetLoader("data/raw/synthetic_mental_health_dataset.csv")

    student_df = student_loader.load()
    mental_df = mental_loader.load()

    inspect_df("STUDENT DATABASE",student_df)
    inspect_df("MENTAL HEALTH DATABASE", mental_df)

    validate_mapping("student", student_df)
    validate_mapping("mental", mental_df)

    student_clean = standardize_df(student_df, "student")
    mental_clean = standardize_df(mental_df, "mental")

    # print(student_clean.head())
    # print(mental_clean.head())

    X_student, y_student = split_features_target(student_clean, TARGET_MAP["student"])
    X_mental, y_mental = split_features_target(mental_clean, TARGET_MAP["mental"])

    print("Splitting Features")
    print("Student:", X_student.shape, y_student.shape)
    print("Mental:", X_mental.shape, y_mental.shape)
    print("Split Completed")

    print("Student X cols:", X_student.columns.tolist())
    print("Mental X cols:", X_mental.columns.tolist())


if __name__ == "__main__":
    main()

