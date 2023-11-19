# Zero Shot Experiment Results Log

## Program

| Index | Program                       | Code                              |
|-------|-------------------------------|-----------------------------------|
| 1     | process.py                    | [click](code/process.py)          |
| 2     | finetune.py                   | [click](code/finetune.py)         |
| 3     | zero-shot.py                  | [click](code/zero-shot.py)        |

For zero-shot evaluation, remember to simultaneously run three categories of zero-shot evaluation on three different GPU devices to save time.

## Process (Use download source dataset)

| Index | Dataset Category              | Log                               |
|-------|-------------------------------|-----------------------------------|
| 1     | CDs and Vinyl                 | [Log](process/CDs.log)            |
| 2     | Clothing, Shoes and Jewelry   | [Log](process/Clothing.log)       |
| 3     | Automotive                    | [Log](process/Automotive.log)     |
| 4     | Cell Phones and Accessories   | [Log](process/Cell.log)           |
| 5     | Electronics                   | [Log](process/Electronics.log)    |
| 6     | Home and Kitchen              | [Log](process/Kitchen.log)        |
| 7     | Movies and TV                 | [Log](process/Movies.log)         |
| 8     | Grocery and Gourmet Food      | [Log](process/Grocery.log)        |
| 9     | Industrial and Scientific     | [Log](process/Scientific.log)     |
| 10    | All Beauty                    | [Log](process/Beauty.log)         |
| 11    | Appliances                    | [Log](process/Appliances.log)     |
| 12    | Books                         | [Log](process/Books.log)          |
| 13    | Gift Cards                    | [Log](process/Gift.log)           |
| 14    | Kindle Store                  | [Log](process/Kindle.log)         |
| 15    | Luxury Beauty                 | [Log](process/Luxury.log)         |
| 16    | Amazon Fashion                | [Log](process/Fashion.log)        |
| 17    | Patio Lawn and Garden         | [Log](process/Garden.log)         |
| 18    | Sports and Outdoors           | [Log](process/Sports.log)         |
| 19    | Arts Crafts and Sewing        | [Log](process/Arts.log)           |
| 20    | Video Games                   | [Log](process/Video.log)          |
| 21    | Musical Instruments           | [Log](process/Instruments.log)    |
| 22    | Office Products               | [Log](process/Office.log)         |
| 23    | Pet Supplies                  | [Log](process/Pet.log)            |
| 24    | Prime Pantry                  | [Log](process/Pantry.log)         |
| 25    | Software                      | [Log](process/Software.log)       |
| 26    | Magazine Subscriptions        | [Log](process/Magazine.log)       |
| 27    | Tools and Home Improvement    | [Log](process/Tools.log)          |
| 28    | Toys and Games                | [Log](process/Toys.log)           |
| 29    | Digital Music                 | [Log](process/Digital.log)        |

## Zero Shot (Replication on pre-processed dataset on original Github)

| Index | Dataset Category              | Log                               | GPU Utilization                       | Evaluation                            |
|-------|-------------------------------|-----------------------------------|---------------------------------------|---------------------------------------|
| 1     | Industrial and Scientific     | [Log](zeroShot/Scientific.log)    | [GPU](zeroShot/Scientific_gpu.log)    | [Met](zeroShot/Scientific_eva.log)    |
| 2     | Arts Crafts and Sewing        | [Log](zeroShot/Arts.log)          | [GPU](zeroShot/Arts_gpu.log)          | [Met](zeroShot/Arts_eva.log)          |
| 3     | Video Games                   | [Log](zeroShot/Games.log)         | [GPU](zeroShot/Games_gpu.log)         | [Met](zeroShot/Games_eva.log)         |
| 4     | Musical Instruments           | [Log](zeroShot/Instruments.log)   | [GPU](zeroShot/Instruments_gpu.log)   | [Met](zeroShot/Instruments_eva.log)   |
| 5     | Office Products               | [Log](zeroShot/Office.log)        | [GPU](zeroShot/Office_gpu.log)        | [Met](zeroShot/Office_eva.log)        |
| 6     | Pet Supplies                  | [Log](zeroShot/Pet.log)           | [GPU](zeroShot/Pet_gpu.log)           | [Met](zeroShot/Pet_eva.log)           |

### Evaluation

| Index | Dataset Category              | NDCG@10   | Recall@10 | NDCG@50   | Recall@50 | MRR       | AUC       |
|-------|-------------------------------|-----------|-----------|-----------|-----------|-----------|-----------|
| 1     | Industrial and Scientific     | 0.08946   | 0.13028   | 0.10550   | 0.203841  | 0.08196   | 0.73164   |
| 2     | Arts Crafts and Sewing        | 0.07228   | 0.11911   | 0.08547   | 0.179381  | 0.06209   | 0.76938   |
| 3     | Video Games                   | 0.03322   | 0.05815   | 0.04615   | 0.117740  | 0.02993   | 0.78776   |
| 4     | Musical Instruments           | 0.04158   | 0.07142   | 0.05227   | 0.120373  | 0.03585   | 0.72126   |
| 5     | Office Products               | 0.05513   | 0.08489   | 0.06256   | 0.134914  | 0.04904   | 0.66997   |
| 6     | Pet Supplies                  | 0.05231   | 0.07780   | 0.06256   | 0.124517  | 0.04727   | 0.74452   |

## Zero Shot (Further exploration on different recommendation scenarios)

| Index | Dataset Category              | Log                               | GPU Utilization                       | Evaluation                            |
|-------|-------------------------------|-----------------------------------|---------------------------------------|---------------------------------------|
| 1     | CDs and Vinyl                 | [Log](zeroShot_I/CDs.log)         | [GPU](zeroShot_I/CDs_gpu.log)         | [Met](zeroShot_I/CDs_eva.log)         |
| 2     | Industrial and Scientific     | [Log](zeroShot_I/Scientific.log)  | [GPU](zeroShot_I/Scientific_gpu.log)  | [Met](zeroShot_I/Scientific_eva.log)  |
| 3     | All Beauty                    | [Log](zeroShot_I/Beauty.log)      | [GPU](zeroShot_I/Beauty_gpu.log)      | [Met](zeroShot_I/Beauty_eva.log)      |
| 4     | Appliances                    | [Log](zeroShot_I/Appliances.log)  | [GPU](zeroShot_I/Appliances_gpu.log)  | [Met](zeroShot_I/Appliances_eva.log)  |
| 5     | Books                         | [Log](zeroShot_I/Books.log)       | [GPU](zeroShot_I/Books_gpu.log)       | [Met](zeroShot_I/Books_eva.log)       |
| 6     | Gift Cards                    | [Log](zeroShot_I/Gift.log)        | [GPU](zeroShot_I/Gift_gpu.log)        | [Met](zeroShot_I/Gift_eva.log)        |
| 7     | Kindle Store                  | [Log](zeroShot_I/Kindle.log)      | Out of GPU Memory                     | None                                  | 
| 8     | Luxury Beauty                 | [Log](zeroShot_I/Luxury.log)      | [GPU](zeroShot_I/Luxury_gpu.log)      | [Met](zeroShot_I/Luxury_eva.log)      |
| 9     | Amazon Fashion                | [Log](zeroShot_I/Fashion.log)     | [GPU](zeroShot_I/Fashion_gpu.log)     | [Met](zeroShot_I/Fashion_eva.log)     |
| 10    | Patio Lawn and Garden         | [Log](zeroShot_I/Garden.log)      | [GPU](zeroShot_I/Garden_gpu.log)      | [Met](zeroShot_I/Garden_eva.log)      |
| 11    | Sports and Outdoors           | [Log](zeroShot_I/Sports.log)      | [GPU](zeroShot_I/Sports_gpu.log)      | [Met](zeroShot_I/Sports_eva.log)      | 
| 12    | Arts Crafts and Sewing        | [Log](zeroShot_I/Arts.log)        | [GPU](zeroShot_I/Arts_gpu.log)        | [Met](zeroShot_I/Arts_eva.log)        |
| 13    | Video Games                   | [Log](zeroShot_I/Video.log)       | [GPU](zeroShot_I/Video_gpu.log)       | [Met](zeroShot_I/Video_eva.log)       |
| 14    | Musical Instruments           | [Log](zeroShot_I/Instruments.log) | [GPU](zeroShot_I/Instruments_gpu.log) | [Met](zeroShot_I/Instruments_eva.log) |
| 15    | Office Products               | [Log](zeroShot_I/Office.log)      | [GPU](zeroShot_I/Office_gpu.log)      | [Met](zeroShot_I/Office_eva.log)      |
| 16    | Pet Supplies                  | [Log](zeroShot_I/Pet.log)         | [GPU](zeroShot_I/Pet_gpu.log)         | [Met](zeroShot_I/Pet_eva.log)         |
| 17    | Prime Pantry                  | [Log](zeroShot_I/Pantry.log)      | [GPU](zeroShot_I/Pantry_gpu.log)      | [Met](zeroShot_I/Pantry_eva.log)      |
| 18    | Software                      | [Log](zeroShot_I/Software.log)    | [GPU](zeroShot_I/Software_gpu.log)    | [Met](zeroShot_I/Software_eva.log)    |
| 19    | Magazine Subscriptions        | [Log](zeroShot_I/Magazine.log)    | [GPU](zeroShot_I/Magazine_gpu.log)    | [Met](zeroShot_I/Magazine_eva.log)    |
| 20    | Tools and Home Improvement    | [Log](zeroShot_I/Tools.log)       | [GPU](zeroShot_I/Tools_gpu.log)       | [Met](zeroShot_I/Tools_eva.log)       |
| 21    | Toys and Games                | [Log](zeroShot_I/Toys.log)        | [GPU](zeroShot_I/Toys_gpu.log)        | [Met](zeroShot_I/Toys_eva.log)        |
| 22    | Digital Music                 | [Log](zeroShot_I/Digital.log)     | [GPU](zeroShot_I/Digital_gpu.log)     | [Met](zeroShot_I/Digital_eva.log)     |

### Evaluation

| Index | Dataset Category              | NDCG@10   | Recall@10 | NDCG@50   | Recall@50 | MRR       | AUC       |
|-------|-------------------------------|-----------|-----------|-----------|-----------|-----------|-----------|
| 1     | CDs and Vinyl                 | 0.03716   | 0.06306   | 0.04672   | 0.10640   | 0.03222   | 0.82979   |
| 2     | Industrial and Scientific     | 0.08059   | 0.12104   | 0.09907   | 0.20521   | 0.07403   | 0.72917   |
| 3     | All Beauty                    | 0.95673   | 0.95673   | 0.96440   | 1.0       | 0.95761   | 0.96081   |
| 4     | Appliances                    | 0.96100   | 0.96100   | 0.96938   | 1.0       | 0.96267   | 0.97810   |
| 5     | Books                         | 0.99583   | 0.99583   | 0.99657   | 1.0       | 0.99592   | 0.99623   |
| 6     | Gift Cards                    | 0.87027   | 0.87027   | 0.90036   | 0.98484   | 0.87919   | 0.97633   |
| 8     | Luxury Beauty                 | 0.71231   | 0.71231   | 0.78424   | 1.0       | 0.73149   | 0.99699   |
| 9     | Amazon Fashion                | 0.95625   | 1.0       | 0.95625   | 1.0       | 0.94167   | 0.99028   | 
| 10    | Patio Lawn and Garden         | 0.99975   | 0.99975   | 0.99975   | 0.99975   | 0.99975   | 0.99975   |
| 11    | Sports and Outdoors           | 1.0       | 1.0       | 1.0       | 1.0       | 1.0       | 1.0       |
| 12    | Arts Crafts and Sewing        | 0.67723   | 0.67723   | 0.75620   | 1.0       | 0.69740   | 0.99975   |
| 13    | Video Games                   | 1.0       | 1.0       | 1.0       | 1.0       | 1.0       | 1.0       |
| 14    | Musical Instruments           | 0.68486   | 0.68486   | 0.76196   | 1.0       | 0.70455   | 0.99948   |
| 15    | Office Products               | 0.72014   | 0.72014   | 0.78861   | 1.0       | 0.73763   | 0.99983   |
| 16    | Pet Supplies                  | 0.99966   | 1.0       | 0.99966   | 1.0       | 0.99957   | 0.99999   |
| 17    | Prime Pantry                  | 0.99964   | 0.99964   | 0.99964   | 0.99964   | 0.99964   | 0.99964   |
| 18    | Software                      | 0.99004   | 0.99004   | 0.99004   | 0.99004   | 0.99005   | 0.99020   |
| 19    | Magazine Subscriptions        | 0.93750   | 0.93750   | 0.9375    | 0.9375    | 0.93805   | 0.94400   |
| 20    | Tools and Home Improvement    | 0.99997   | 0.99990   | 0.99998   | 0.99998   | 0.99998   | 0.99998   |
| 21    | Toys and Games                | 0.99994   | 1.0       | 0.99994   | 1.0       | 0.99992   | 0.99999   |
| 22    | Digital Music                 | 0.59543   | 0.59543   | 0.69441   | 1.0       | 0.62071   | 0.99937   |

## Recommend on Seen Data

| Index | Dataset Category              | Log                               | GPU Utilization                       | Evaluation                            |
|-------|-------------------------------|-----------------------------------|---------------------------------------|---------------------------------------|
| 1     | Automotive                    | [Log](zeroShot_I/Automotive.log)  | [GPU](zeroShot_I/Automotive_gpu.log)  | [Met](zeroShot_I/Automotive_eva.log)  |
| 2     | Cell Phones and Accessories   | [Log](zeroShot_I/Cell.log)        | [GPU](zeroShot_I/Cell_gpu.log)        | [Met](zeroShot_I/Cell_eva.log)        |
| 3     | Clothing, Shoes and Jewelry   | [Log](zeroShot_I/Clothing.log)    | Out of GPU Memory                     | None                                  |
| 4     | Electronics                   | [Log](zeroShot_I/Electronics.log) | [GPU](zeroShot_I/Electronics_gpu.log) | [Met](zeroShot_I/Electronics_eva.log) |
| 5     | Grocery and Gourmet Food      | [Log](zeroShot_I/Grocery.log)     | [GPU](zeroShot_I/Grocery_gpu.log)     | [Met](zeroShot_I/Grocery_eva.log)     |
| 6     | Home and Kitchen              | [Log](zeroShot_I/Kitchen.log)     | Out of GPU Memory                     | None                                  |
| 7     | Movies and TV                 | [Log](zeroShot_I/Movies.log)      | [GPU](zeroShot_I/Movies_gpu.log)      | [Met](zeroShot_I/Movies_eva.log)      |

### Evaluation

| Index | Dataset Category              | NDCG@10   | Recall@10 | NDCG@50   | Recall@50 | MRR       | AUC       |
|-------|-------------------------------|-----------|-----------|-----------|-----------|-----------|-----------|
| 1     | Automotive                    | 0.02505   | 0.04048   | 0.03123   | 0.068561  | 0.02235   | 0.72945   |
| 2     | Cell Phones and Accessories   | 0.01387   | 0.02526   | 0.02106   | 0.058893  | 0.01298   | 0.76478   |
| 3     | Clothing, Shoes and Jewelry   | -         | -         | -         | -         | -         | -         |
| 4     | Electronics                   | 0.02022   | 0.03133   | 0.02401   | 0.048560  | 0.01801   | 0.71861   |
| 5     | Grocery and Gourmet Food      | 0.06864   | 0.11194   | 0.08008   | 0.163593  | 0.05851   | 0.73655   |
| 6     | Home and Kitchen              | -         | -         | -         | -         | -         | -         |
| 7     | Movies and TV                 | 0.06299   | 0.10302   | 0.07037   | 0.136219  | 0.05262   | 0.75127   |

## Finetuning

| Index | Dataset Category              | Log                               | GPU Utilization                       | Evaluation                            |
|-------|-------------------------------|-----------------------------------|---------------------------------------|---------------------------------------|
| 1     | CDs and Vinyl                 | [Log](finetuning/CDs.log)         | [GPU](finetuning/CDs_gpu.log)         | [Met](finetuning/CDs_eva.log)         |
| 2     | Industrial and Scientific     | [Log](finetuning/Scientific.log)  | [GPU](finetuning/Scientific_gpu.log)  | [Met](finetuning/Scientific_eva.log)  |
