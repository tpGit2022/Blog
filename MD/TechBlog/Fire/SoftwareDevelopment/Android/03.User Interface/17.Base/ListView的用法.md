1. ListView的单条刷新。
```
private void updateSingleRow(ListView listView, int id) {
        int startShowIndex=listView.getFirstVisiblePosition();
        int endShowIndex=listView.getLastVisiblePosition();
        //获取当前屏幕中显示的数据id的开始和结束值，只有当设定的id值在屏幕范围之内时才需要重新绘制否则没有必要
        if(id>=startShowIndex&&id<=endShowIndex){
            View view=listView.getChildAt(id-startShowIndex);
            View itemView=listView.getAdapter().getView(id, view, listView);
            TextView titleTv=(TextView) itemView.findViewById(R.id.titleText);
            TextView abstractNTv=(TextView) itemView.findViewById(R.id.contentText);
            //TODO
        }
```

移除ListView自带的子item的分割线`android:divider="@null"`

2. ListView的单条刷新。
单条刷新
```
    /**
     * 更新单个item，避免刷新所有数据源
     *
     * @param listview
     * @param id
     */
    public void updateSingleRow(ListView listview, int id) {
        if (listview != null) {
            int visibleposition = listview.getFirstVisiblePosition();
            if (id >= visibleposition && id <= listview.getLastVisiblePosition()) {
                View view = listview.getChildAt(id - visibleposition);
                ViewHolder holder = (ViewHolder) view.getTag();
                //利用holder做更新视图的操作
            }
        }
    }
```