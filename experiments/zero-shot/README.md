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

## Finetuning

| Index | Dataset Category              | Log                               | GPU Utilization                       | Evaluation                            |
|-------|-------------------------------|-----------------------------------|---------------------------------------|---------------------------------------|
| 1     | CDs and Vinyl                 | [Log](finetuning/CDs.log)         | [GPU](finetuning/CDs_gpu.log)         | [Met](finetuning/CDs_eva.log)         |
| 2     | Industrial and Scientific     | [Log](finetuning/Scientific.log)  | [GPU](finetuning/Scientific_gpu.log)  | [Met](finetuning/Scientific_eva.log)  |
