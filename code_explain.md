```
.
├── __init__.py
├── add_e3po_to_environment.py
├── approaches  # 算法文件夹，每个子文件夹代表一种算法
│   ├── cubemap # 每个算法文件夹包括一个算法类（需要自己实现类方法），和一个yml配置文件
│   ├── custom_eac
│   ├── erp
│   └── freedom
├── data        # 预处理时的基本脚本程序，在算法类中被调用
│   ├── __init__.py
│   ├── __pycache__
│   ├── base_data.py
│   ├── on_demand_data.py
│   └── transcoding_data.py
├── decision    # 下载决策时的基本脚本程序，在算法类中被调用
│   ├── __init__.py
│   ├── __pycache__
│   ├── base_decision.py
│   ├── on_demand_decision.py
│   └── transcoding_decision.py
├── e3po.yml    # 系统配置文件一般不做修改，注意更换测试组时需要更改group_name
├── evaluation  # 评估时的基本脚本程序，评估时被调用
│   ├── __init__.py
│   ├── __pycache__
│   ├── base_eval.py
│   ├── on_demand_eval.py
│   └── transcoding_eval.py
├── log         # 日志文件
│   └── group_1
├── make_decision.py      # 入口程序
├── make_evaluation.py    # 入口程序
├── make_preprocessing.py # 入口程序
├── result                # decision和evaluation后的结果
│   └── group_1
├── source                # 视频源
│   ├── motion_trace      
│   └── video             # preprocessing后的结果数据
└── utils           
    ├── __init__.py
    ├── __pycache__
    ├── data_utilities.py
    ├── decision_utilities.py   # 含可更改的方法
    ├── evaluation_utilities.py
    ├── json.py
    ├── logger.py
    ├── misc.py
    ├── motion_trace.py
    ├── options.py
    ├── projection_utilities.py
    ├── psnr_ssim.py
    └── registry.py
```