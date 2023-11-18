## Data Preprocessing
1. Open time_extract.py, set up path and category, and run it to extract time information from user sequence

2. Open merge_time_data_experiment_1.py, set up path and category, and run it to merge time information from step 1 to meta_data


## Experiment 1 Setup
- For lightning_pretrain.py and finetune.py, update max_attr_num from 3 to 6
```
config.max_attr_num = 6
```