
import os
from TextSummaizer.logging import logger
from TextSummaizer.config.configuration import DataValidationConfig

class DataValiadtion:
    def __init__(self, config: DataValidationConfig):
        self.config = config


    
    def validate_all_files_exist(self)-> bool:
        try:            

            all_files = os.listdir(os.path.join("artifacts","data_ingetion","samsum_dataset"))
            validation_status = True
            dataset_path = os.path.join("artifacts","data_ingetion","samsum_dataset")

            print(f"🔍 Checking dataset path: {os.path.abspath(dataset_path)}")
            print(f"🔍 Expected files: {self.config.ALL_REQUIRED_FILES}")

            if not os.path.exists(dataset_path):
                print(f"❌ ERROR: Directory '{dataset_path}' does not exist!")
                validation_status = False
            else:
                existing_files = set(os.listdir(dataset_path))
                missing_files = [file for file in self.config.ALL_REQUIRED_FILES if file not in existing_files]

                if missing_files:
                    print(f"❌ Missing files: {missing_files}")
                    validation_status = False
                else:
                    print(f"✅ All required files are present.")

            # ✅ Write status only once (instead of inside the loop)
            with open(self.config.STATUS_FILE, 'w') as f:
                f.write(f"Validation status: {validation_status}")

            return validation_status

        except Exception as e:
            raise e

            
       