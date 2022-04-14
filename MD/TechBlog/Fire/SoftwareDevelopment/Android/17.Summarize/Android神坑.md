1. 获取资源图片的问题
        ```
            if(Build.VERSION.SDK_INT>=Build.VERSION_CODES.LOLLIPOP){
            draw_undoclassroom = activity.getResources().getDrawable(
                    R.drawable.schedule_changeclass_disable, null);
            draw_undoclassroom.setBounds(0, 0, 30, 30);
        }else{
            draw_undoclassroom=activity.getResources().getDrawable(R.drawable.schedule_changeclass_disable);
            draw_undoclassroom.setBounds(0, 0, 30, 30);
        }
        ```
2. Andorid 6.0移除了HttpClient的支持，使用HttpClient做好版本判断，非要使用建议引入`org.apache.http.legacy` 包。