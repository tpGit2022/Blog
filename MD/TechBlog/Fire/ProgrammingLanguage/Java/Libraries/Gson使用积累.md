
1. 转为List类型，需要借助特定的Type
```
Type type = new TypeToken<ClassTypeName>(){}.getType();
Class cls = gson.fromJson(json, type);
```

2. Map 对象的转化

```
Gson mapGson = new GsonBuilder().enableComplexMapKeySerialization().create();
Type type = new TypeToken<Map<ObjectClassName, ObjectClassName>>() {}.getType();
mapGson.fromJson(json,type)
```
