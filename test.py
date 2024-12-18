import os

root_path = r'E:\Object_Detection\DataSet\FDDB\FDDB-folds\FDDB-folds\FDDB-folds'
# FDDB-fold-01.txt, or FDDB-fold-01-ellipseList.txt
file_paths = ['FDDB-fold']
output_image = '../FDDB/image.txt'
output_label = '../FDDB/label.txt'
# 使用列表作为写入的时候， 会出现
# PermissionError: [Errno 13] Permission denied: '/'类型的错误
# 也许只是我把列表写成了str类型
output_path = [output_image, output_label]


# merge_files(file_paths, output_path)
def merge_files(file_paths: list[str], output_path: list[str]) -> None:
    merged_content1 = ""
    merged_content2 = ""
    FDDB_fold_image = []
    FDDB_fold_label = []

    for idx in range(10):
        path_image = os.path.join(root_path, file_paths[0] + '-' + "{:02d}".format(idx + 1) + '.txt')
        FDDB_fold_image.append(path_image)
        path_label = os.path.join(root_path, file_paths[0] + '-' + "{:02d}".format(idx + 1)
                                  + '-' + 'ellipseList' + '.txt')
        FDDB_fold_label.append(path_label)

    for file_path in FDDB_fold_image:
        with open(file_path, 'r') as file:
            content1 = file.read()
            merged_content1 += content1

    for file_path in FDDB_fold_label:
        with open(file_path, 'r') as file:
            content2 = file.read()
            merged_content2 += content2

    with open(output_path[0], 'w') as output_file:
        output_file.write(merged_content1)

    with open(output_path[1], 'w') as output_file:
        output_file.write(merged_content2)


def main():
    # 主要执行逻辑代码
    print("Hello, World!")
    merge_files(file_paths, output_path)


# 检查是否直接执行脚本
if __name__ == "__main__":
    main()
