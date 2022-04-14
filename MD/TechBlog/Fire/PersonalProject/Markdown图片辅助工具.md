[TOC]

> 实现一个用于生成符合MarkDown语法的的插入图片链接的小软件工具  

# 更新记录

##  update  2017/02/09 

**通过配置文件的方式设置图片的存储路径**

通过读取配置中设置的路径作为图片的存储路径。由于要打包成jar，稍微注意下路径的问题同时别忘记了中文编码格式的问题记得将字符集设置为utf-8，实现代码如下。
```
/**
	 * 获取配置文件中的图片的路径，若获取失败将当前目录作为存储目录。
	 * @param fileName
	 * @param key
	 * @return
	 */
	public  String getStorePath(String fileName, String key) {
		//markdowntool.config
		Properties props = new Properties();
		String value = null;
		try {
			InputStreamReader isr = new InputStreamReader(new FileInputStream(fileName),"UTF-8");
			props.load(isr);
			value = props.getProperty(key);
		} catch (Exception e) {
			e.printStackTrace();
		}
		return value;
	}
	//做好判断避免异常出现
	strFileDir=getStorePath("MarkDownTool.config", "PicPath");
			if(null==strFileDir||"".equals(strFileDir)){
				strFileDir="D:/Arsenal/Blog/Picture";
			}
```

配置文件`MarkDownTool.config`的内容如下:
```
PicPath=D:/Arsenal/Blog/Picture
```

`MarkDownTool.config`必须和生成的jar包处在同一级目录下面。

 ***Java实现生成符合Markdown插入本地图片链接的工具***  
## update 2016/12/26

 *添加直接复制图片时生成MarkDown图片链接功能*  
 
 主要是当剪切板中数据类型匹配`DataFlavor.javaFileListFlavor`,代表复制的是文件，将其强制转化为`List<File>`类型。下面代码其实不完善没有做是否是图片类型文件的判断。
 ```
 if(trans.isDataFlavorSupported(DataFlavor.javaFileListFlavor)){
				System.out.println("剪切板中是filelist数据");

				try {
					@SuppressWarnings("unchecked")
					List<File> filelist=(List<File>) trans.getTransferData(DataFlavor.javaFileListFlavor);
					if(filelist!=null&&filelist.size()>0){
						for(File file:filelist){
							System.out.println("文件名称="+file.getName()+"文件地址"+file.getAbsolutePath());
							File resultfile=mImageUtils.copyFile(file);
							if(resultfile!=null)
							writeToClip(markdownPicLink(resultfile));
						}
					}
				} catch (UnsupportedFlavorException e) {
					// TODO Auto-generated catch block
					e.printStackTrace();
				} catch (IOException e) {
					// TODO Auto-generated catch block
					e.printStackTrace();
				}
			}
 ```


## update 2016/12/20

 *先考虑实现最重要的功能，剪切板图片的读取本地保存和链接生成*



整个项目的结构如下图，目前总共200行代码左右。

![20161220194504.png](../../Pictures\20161220\20161220194504.png)  
`Clipboard`负责剪切板相关操作  
`ImageUtils`负责图片存储相关操作(暂时没有做拉伸裁剪等等操作)
`Mainclass` 这个就不用多说了。

 **剪切板操作**  
 要实现的剪切板的操作从剪切板中读取数据如果数据类型是图片类型保存为指定目录，同时生成该图片的MarkDown语法格式链接，同时将该链接写入剪切板中。Java里面用于操作剪切板的类`Clipboard` ,`Transferable`，`DataFlavor`。
 新建`ClipManager`类用于操作剪切板，代码如下
 ```
 public class ClipManager {
	private Clipboard clip;
	private Transferable trans;
	private ClipManager mClipManager;
	private ImageUtils mImageUtils;
	public ClipManager() {
		if (mClipManager == null) {
			clip = Toolkit.getDefaultToolkit().getSystemClipboard();
			mImageUtils=new ImageUtils();
		}
	}

	// 获取剪切板中的内容
	public String getClipboardText() {
		trans = clip.getContents(null);
		if (trans != null) {
			// 检查内容是否是文本类型
			if (trans.isDataFlavorSupported(DataFlavor.stringFlavor)) {
				try {
					return (String) trans
							.getTransferData(DataFlavor.stringFlavor);
				} catch (UnsupportedFlavorException e) {
					e.printStackTrace();
				} catch (IOException e) {
					e.printStackTrace();
				}
			}
		}
		return null;
	}
	/**
	 * 获取剪切板中的图像，保存至本地文件，同时同符合MarkDown格式的语法填充剪切板
	 */
	public Image getClipboardImg(){
		trans=clip.getContents(null);
		if(trans!=null){
			if(trans.isDataFlavorSupported(DataFlavor.imageFlavor)){
				try {
					//从剪切板中获取到的图片数据
					Image img=(Image) trans.getTransferData(DataFlavor.imageFlavor);
					File file=mImageUtils.writeToFile(img);
					writeToClip(markdownPicLink(file));
					return img;
				} catch (UnsupportedFlavorException e) {
					// TODO Auto-generated catch block
					e.printStackTrace();
				} catch (IOException e) {
					// TODO Auto-generated  catch block
					e.printStackTrace();
				}
				System.out.println("剪切板中的图像数据");
			}
		}
		return null;
	}
	/**
	 * 将MarkDown链接复制至系统剪切板中
	 */
	public void writeToClip(String content){
		trans=new StringSelection(content);
		clip.setContents(trans, null);
	}
	/**
	 * 生成符合MarkDown语法的插入图片的链接形式
	 * MarkDown格式
	 * ![描述信息](D:/Arsenal/Blog/Picture/20161219/20161219173226.png)
	 * @param file
	 * @return
	 */
	public String markdownPicLink(File file){
		StringBuffer sb=new StringBuffer();
		sb.append("!").append("["+file.getName()+"]").append("("+file.getAbsolutePath()+")");
		return sb.toString();
	}
 ```

**图片的操作**  
 通过*javax.imageio*包下面的 *ImageIO* 完成Image对象的存储。ImageUtils中的变量`strFileDir`定义存放图片的根目录，所有截取的图片以当前日期时间为名以日期为文件夹存放在`strFileDir`路径下。具体代码如下：
 ```
 /**
  * @author seeksky
  * @version 2016年12月19日
  * @function
  * 完成图像的保存 (裁剪 旋转 缩放暂无完成) 功能
  */
 public class ImageUtils {
 	//D:\Arsenal\Blog\Picture
 	//E:\MyBlogs\MD\Picture
 	private final String strFileDir="E:/MyBlogs/MD/Picture";
 	private File fileDir;//截图文件存储根目录
 	private final String fileSuffix=".png";
 	private SimpleDateFormat fileSDF;
 	private ImageUtils imageUtils;
 	public ImageUtils(){
 		if(imageUtils==null){
 			//格式化时间
 //			格式化时间
 			fileSDF=new SimpleDateFormat("yyyyMMddHHmmss", Locale.CHINA);
 			if(fileDir==null){
 				fileDir=new File(strFileDir);
 			}
 			if(!fileDir.exists()){
 				fileDir.mkdirs();
 			}
 		}
 	}
 	/**
 	 * 保存图片至文件
 	 * @param img
 	 */
 	public File writeToFile(Image img) {
 		File file=newFile();
 		int wid = img.getWidth(null);
 		int hei = img.getHeight(null);
 		BufferedImage bi = new BufferedImage(wid, hei,
 				BufferedImage.TYPE_4BYTE_ABGR_PRE);
 		Graphics g = bi.getGraphics();
 		g.drawImage(img, 0, 0, null);
 		try {
 			ImageIO.write(bi, "png",file);
 		} catch (IOException e) {
 			// TODO Auto-generated catch block
 			e.printStackTrace();
 			System.err.println(e.getCause() + e.getMessage());
 		}
 		return file;
 	}
 	/**
 	 * 生成以日期为格式的文件
 	 * @return
 	 */
 	public File newFile(){
 		Calendar calendar=Calendar.getInstance();
 		String strfilename=fileSDF.format(calendar.getTime());
 		String strdirname=strfilename.substring(0, 8);
 		File file=new File(strFileDir+"/"+strdirname+"/"+strfilename+fileSuffix);
 		if(!file.getParentFile().exists()){
 			file.getParentFile().mkdirs();//父目录不存在则创建
 		}
 		if(!file.exists()){
 			try {
 				file.createNewFile();
 			} catch (IOException e) {
 				// TODO Auto-generated catch block
 				e.printStackTrace();
 			}
 		}
 		return file;
 	}
 }
 ```
将项目打包成可运行的jar文件。双击便可实现从剪切板中读取图片并将图片存储至本地。这样发现还是不是很方便，于是考虑为jar设定全局快捷键。搜索了下貌似Java不能直接设置windows下面的全局快捷键(如果你发现了请告��我)，想起了有个叫`AutoHotKey`好像说是可以完成Windows下面的全局热键设置，从官方网站下载看了下文档好像要自己写什么awk脚本感觉麻烦了点，时间成本略高。突然想到Windows好像可以快捷方式设置快捷键。于是在桌面创建了MarkDownPic.jar的快捷方式，同时右键添加快捷键  
![20161220200931.png](../../Pictures\20161220\20161220200931.png)。  
这样便可以使用全局快捷键Ctrl+Alt+Shift+C生成图片链接了(个人测试快捷方式需要放在桌面上全局热键才有效)。


## update 2016/12/15

***思路***

从剪切板获取图片，显示图片并显示为可编辑状态，调整后生成MarkDown语法链接。
主要的难点在于
1. 如何从剪切板获取图片
2. 如何显示和编辑图片
3. 如何为小工具设置可用的全局快捷键

***实践解决***
一向对Java的GUI编程不熟悉。以"Java 显示图片的控件"搜索了半天，没发现Java的GUI编程中可以直接显示图片的控件。
于是换搜索关键字为"Java实现图片查看器",或者"Java 图片编辑器" ，收获颇丰。第二个问题解决。


# 参考链接
http://blog.sina.com.cn/s/blog_62cd5a980100mamy.html
