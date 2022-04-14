# 文件重命名
下载下来的视频，文本难免带有多余的字符，利用下方脚本即可批量重命名

```
# 路径或文件中的中括号会导致问题[],匹配通配符不知道是什么鬼
# 第 \u7b2c  集 \u96c6 季 \u5b63 话 \u8bdd
$file_path = "Q:\04. Videos\Anime\Re：从零开始的异世界生活"
$file_reg = "\[[0-9]{1,3}\]"
$file_baseName = "Re：从零开始的异世界生活-720p-"
$file_ext_list = '.mkv', '.mp4', '.3gp', '.rmvb', '.ass'
$temp_file = $file_path + "\temp.txt"
cd -literalpath $file_path
Get-ChildItem  -literalpath  $file_path | ForEach-Object {
    $extension = $_.Extension
    Write-Output $_.BaseName
    # echo $_.BaseName >> $temp_file
      If ($file_ext_list -contains $_.Extension) {
            Write-Output "base name is $_"
            If ($_.BaseName -match $file_reg -and (-not [String]::IsNullOrEmpty($matches[0]))) {
                    $temp_name = $matches[0]
                    Write-Output "temp name is $temp_name"
                    If ($temp_name -match "[0-9]{1,3}" -and -not [String]::IsNullOrEmpty($matches[0])) {
                            Write-Output numer is  $matches[0]
                            $new_file_name = $file_baseName + "第" + $matches[0] + "集" + $_.Extension
                            $new_full_file_path_name = $_.DirectoryName + "\" + $new_file_name
                            # Write-Output $_.FullName
                            # Write-Output $new_full_file_path_name
                            # Write-Output $_.FullName
                            $tips = "$_. 重命名为  $new_full_file_path_name"
                            Write-Output $tips
                            # echo $tips >> $temp_file
                            Move-Item -literalpath  $_.FullName  -Destination $new_full_file_path_name
                    }
            }     
      }
}
```