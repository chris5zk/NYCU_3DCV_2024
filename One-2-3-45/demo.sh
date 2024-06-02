#!/bin/bash

# 指定要遍歷的資料夾路徑
FOLDER_PATH="./inputs/"

# 指定要執行的程式
PROGRAM="run.py"

# 檢查資料夾是否存在
if [ ! -d "$FOLDER_PATH" ]; then
  echo "資料夾 $FOLDER_PATH 不存在"
  exit 1
fi

# 遍歷資料夾中的每個檔案
for FILE in "$FOLDER_PATH"/*; do
  echo "running for $FILE"
  # 檢查是否為檔案（而不是資料夾）
  if [ -f "$FILE" ]; then
    # 執行程式並將檔案路徑作為參數傳遞
    python "$PROGRAM" --img_path "$FILE" --half_precision
  fi
done
