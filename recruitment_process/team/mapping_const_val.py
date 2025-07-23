import pandas as pd
import matplotlib.pyplot as plt

# CSV 파일 읽기
df = pd.read_csv(r'c:\Codessey\recruitment_process\team\area_map.csv')

print(df.head(5))

# ConstructionSite가 1인 좌표만 선택
construction = df[df['ConstructionSite'] == 1]

plt.figure(figsize=(6, 6))
# 회색 네모로 표시
plt.scatter(construction['x'], construction['y'], color='gray', marker='s', s=200, label='Construction Site')

plt.xlabel('x')
plt.ylabel('y')
plt.title('Construction Site Map')

plt.xlim(1, 16)
plt.ylim(1, 16)
plt.xticks(range(1, 17))
plt.yticks(range(1, 17))
plt.grid(True, which='both', linestyle='--', linewidth=0.5)
plt.savefig('area_map.png')
plt.grid(True)
plt.legend()
plt.show()