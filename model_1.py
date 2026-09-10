# 모델링 패키지 가져오기
import os
import torch
import numpy as np
import matplotlib.pyplot as plt


# 디바이스 설정
device = 'cuda' if torch.cuda.is_available() else 'cpu'
print(f"현재 사용중인 디바이스: {device}")