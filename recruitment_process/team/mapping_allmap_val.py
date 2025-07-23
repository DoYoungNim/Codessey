import pandas as pd
import matplotlib.pyplot as plt

# 파일 경로
struct_path = r'c:\Codessey\recruitment_process\team\area_struct.csv'
category_path = r'c:\Codessey\recruitment_process\team\area_category.csv'

# CSV 읽기
struct_df = pd.read_csv(struct_path)
category_df = pd.read_csv(category_path)

# category 기준 병합
merged_df = pd.merge(struct_df, category_df, on='category', how='left')

# 병합 후 컬럼명 공백 제거
merged_df.columns = merged_df.columns.str.strip()

# 시각화 코드
legend_info = {
    'Apartment': {'color': 'blue', 'marker': 's'},
    'Building': {'color': 'green', 'marker': 'o'},
    'MyHome': {'color': 'red', 'marker': '^'},
    'BandalgomCoffee': {'color': 'orange', 'marker': 'D'},
    # None 값을 처리하기 위해 NaN을 추가
    float('nan'): {'color': 'gray', 'marker': 'x'}
}

plt.figure(figsize=(8, 8))

# struct 열의 NaN 값도 처리하기 위해 fillna를 사용
merged_df['struct'] = merged_df['struct'].fillna(float('nan'))

for struct_name, info in legend_info.items():
    if pd.isna(struct_name): # NaN 값을 처리
        subset = merged_df[merged_df['struct'].isna()]
        label_name = 'None'
    else:
        subset = merged_df[merged_df['struct'] == struct_name]
        label_name = struct_name

    plt.scatter(subset['x'], subset['y'],
                color=info['color'], marker=info['marker'], s=100,
                label=label_name)

plt.xlabel('x')
plt.ylabel('y')
plt.title('Area Struct Map')
plt.xlim(1, 16)
plt.ylim(1, 16)
plt.xticks(range(1, 17))
plt.yticks(range(1, 17))
plt.grid(True, linestyle='--', linewidth=0.5)
plt.legend()
plt.tight_layout()
plt.savefig('area_struct_map.png')
plt.show()