[TOC]

AnyTxt 用于文件内容的搜索，配置起来感觉非常繁琐，要手动一下下配置只搜索的目录 而且还要针对每一种文件类型重新添加一遍感觉非常麻烦，遂用ProcessMonitor查找读写的文件，最终确定读写了安装录下 `config.db` 文件，

经过分析 `config.db` 的 `IndexStat` 表中存储相关文件类型和搜索的文件夹，最终得到 sql 如下 执行即可

>> stat 代表该项是否显示 4 显示 5 不显示


```sql
INSERT INTO "main"."IndexStat" ("id", "ext", "stat", "total", "group", "rule") VALUES ('5', '.wps', '4', '9', '0', '<?xml version="1.0" encoding="UTF-8" standalone="yes" ?>
<!DOCTYPE boost_serialization>
<boost_serialization signature="serialization::archive" version="13">
<dataObj class_id="0" tracking_level="0" version="0">
	<m_ruleType>1</m_ruleType>
	<m_qslPaths class_id="1" tracking_level="0" version="0">
		<stdList class_id="2" tracking_level="0" version="0">
			<count>7</count>
			<item_version>0</item_version>
			<item class_id="3" tracking_level="0" version="0">
				<stdString>C:\Users\Walkers\Desktop</stdString>
			</item>
			<item>
				<stdString>D:\SW_TestLog</stdString>
			</item>
			<item>
				<stdString>D:\SW_ThirdLibrarys</stdString>
			</item>
			<item>
				<stdString>E:\MyCode</stdString>
			</item>
			<item>
				<stdString>E:\MyIT</stdString>
			</item>
			<item>
				<stdString>E:\MySDK</stdString>
			</item>
			<item>
				<stdString>E:\MyWorkDir</stdString>
			</item>
		</stdList>
	</m_qslPaths>
</dataObj>
');
INSERT INTO "main"."IndexStat" ("id", "ext", "stat", "total", "group", "rule") VALUES ('6', '.et', '4', '49', '0', '<?xml version="1.0" encoding="UTF-8" standalone="yes" ?>
<!DOCTYPE boost_serialization>
<boost_serialization signature="serialization::archive" version="13">
<dataObj class_id="0" tracking_level="0" version="0">
	<m_ruleType>1</m_ruleType>
	<m_qslPaths class_id="1" tracking_level="0" version="0">
		<stdList class_id="2" tracking_level="0" version="0">
			<count>7</count>
			<item_version>0</item_version>
			<item class_id="3" tracking_level="0" version="0">
				<stdString>C:\Users\Walkers\Desktop</stdString>
			</item>
			<item>
				<stdString>D:\SW_TestLog</stdString>
			</item>
			<item>
				<stdString>D:\SW_ThirdLibrarys</stdString>
			</item>
			<item>
				<stdString>E:\MyCode</stdString>
			</item>
			<item>
				<stdString>E:\MyIT</stdString>
			</item>
			<item>
				<stdString>E:\MySDK</stdString>
			</item>
			<item>
				<stdString>E:\MyWorkDir</stdString>
			</item>
		</stdList>
	</m_qslPaths>
</dataObj>
');
INSERT INTO "main"."IndexStat" ("id", "ext", "stat", "total", "group", "rule") VALUES ('7', '.dps', '4', '4', '0', '<?xml version="1.0" encoding="UTF-8" standalone="yes" ?>
<!DOCTYPE boost_serialization>
<boost_serialization signature="serialization::archive" version="13">
<dataObj class_id="0" tracking_level="0" version="0">
	<m_ruleType>1</m_ruleType>
	<m_qslPaths class_id="1" tracking_level="0" version="0">
		<stdList class_id="2" tracking_level="0" version="0">
			<count>7</count>
			<item_version>0</item_version>
			<item class_id="3" tracking_level="0" version="0">
				<stdString>C:\Users\Walkers\Desktop</stdString>
			</item>
			<item>
				<stdString>D:\SW_TestLog</stdString>
			</item>
			<item>
				<stdString>D:\SW_ThirdLibrarys</stdString>
			</item>
			<item>
				<stdString>E:\MyCode</stdString>
			</item>
			<item>
				<stdString>E:\MyIT</stdString>
			</item>
			<item>
				<stdString>E:\MySDK</stdString>
			</item>
			<item>
				<stdString>E:\MyWorkDir</stdString>
			</item>
		</stdList>
	</m_qslPaths>
</dataObj>
');
INSERT INTO "main"."IndexStat" ("id", "ext", "stat", "total", "group", "rule") VALUES ('8', '.pdf', '4', '1357', '0', '<?xml version="1.0" encoding="UTF-8" standalone="yes" ?>
<!DOCTYPE boost_serialization>
<boost_serialization signature="serialization::archive" version="13">
<dataObj class_id="0" tracking_level="0" version="0">
	<m_ruleType>1</m_ruleType>
	<m_qslPaths class_id="1" tracking_level="0" version="0">
		<stdList class_id="2" tracking_level="0" version="0">
			<count>7</count>
			<item_version>0</item_version>
			<item class_id="3" tracking_level="0" version="0">
				<stdString>C:\Users\Walkers\Desktop</stdString>
			</item>
			<item>
				<stdString>D:\SW_TestLog</stdString>
			</item>
			<item>
				<stdString>D:\SW_ThirdLibrarys</stdString>
			</item>
			<item>
				<stdString>E:\MyCode</stdString>
			</item>
			<item>
				<stdString>E:\MyIT</stdString>
			</item>
			<item>
				<stdString>E:\MySDK</stdString>
			</item>
			<item>
				<stdString>E:\MyWorkDir</stdString>
			</item>
		</stdList>
	</m_qslPaths>
</dataObj>
');
INSERT INTO "main"."IndexStat" ("id", "ext", "stat", "total", "group", "rule") VALUES ('9', '.doc', '4', '81', '0', '<?xml version="1.0" encoding="UTF-8" standalone="yes" ?>
<!DOCTYPE boost_serialization>
<boost_serialization signature="serialization::archive" version="13">
<dataObj class_id="0" tracking_level="0" version="0">
	<m_ruleType>1</m_ruleType>
	<m_qslPaths class_id="1" tracking_level="0" version="0">
		<stdList class_id="2" tracking_level="0" version="0">
			<count>7</count>
			<item_version>0</item_version>
			<item class_id="3" tracking_level="0" version="0">
				<stdString>C:\Users\Walkers\Desktop</stdString>
			</item>
			<item>
				<stdString>D:\SW_TestLog</stdString>
			</item>
			<item>
				<stdString>D:\SW_ThirdLibrarys</stdString>
			</item>
			<item>
				<stdString>E:\MyCode</stdString>
			</item>
			<item>
				<stdString>E:\MyIT</stdString>
			</item>
			<item>
				<stdString>E:\MySDK</stdString>
			</item>
			<item>
				<stdString>E:\MyWorkDir</stdString>
			</item>
		</stdList>
	</m_qslPaths>
</dataObj>
');
INSERT INTO "main"."IndexStat" ("id", "ext", "stat", "total", "group", "rule") VALUES ('10', '.ppt', '4', '45', '0', '<?xml version="1.0" encoding="UTF-8" standalone="yes" ?>
<!DOCTYPE boost_serialization>
<boost_serialization signature="serialization::archive" version="13">
<dataObj class_id="0" tracking_level="0" version="0">
	<m_ruleType>1</m_ruleType>
	<m_qslPaths class_id="1" tracking_level="0" version="0">
		<stdList class_id="2" tracking_level="0" version="0">
			<count>7</count>
			<item_version>0</item_version>
			<item class_id="3" tracking_level="0" version="0">
				<stdString>C:\Users\Walkers\Desktop</stdString>
			</item>
			<item>
				<stdString>D:\SW_TestLog</stdString>
			</item>
			<item>
				<stdString>D:\SW_ThirdLibrarys</stdString>
			</item>
			<item>
				<stdString>E:\MyCode</stdString>
			</item>
			<item>
				<stdString>E:\MyIT</stdString>
			</item>
			<item>
				<stdString>E:\MySDK</stdString>
			</item>
			<item>
				<stdString>E:\MyWorkDir</stdString>
			</item>
		</stdList>
	</m_qslPaths>
</dataObj>
');
INSERT INTO "main"."IndexStat" ("id", "ext", "stat", "total", "group", "rule") VALUES ('11', '.xls', '4', '45', '0', '<?xml version="1.0" encoding="UTF-8" standalone="yes" ?>
<!DOCTYPE boost_serialization>
<boost_serialization signature="serialization::archive" version="13">
<dataObj class_id="0" tracking_level="0" version="0">
	<m_ruleType>1</m_ruleType>
	<m_qslPaths class_id="1" tracking_level="0" version="0">
		<stdList class_id="2" tracking_level="0" version="0">
			<count>7</count>
			<item_version>0</item_version>
			<item class_id="3" tracking_level="0" version="0">
				<stdString>C:\Users\Walkers\Desktop</stdString>
			</item>
			<item>
				<stdString>D:\SW_TestLog</stdString>
			</item>
			<item>
				<stdString>D:\SW_ThirdLibrarys</stdString>
			</item>
			<item>
				<stdString>E:\MyCode</stdString>
			</item>
			<item>
				<stdString>E:\MyIT</stdString>
			</item>
			<item>
				<stdString>E:\MySDK</stdString>
			</item>
			<item>
				<stdString>E:\MyWorkDir</stdString>
			</item>
		</stdList>
	</m_qslPaths>
</dataObj>
');
INSERT INTO "main"."IndexStat" ("id", "ext", "stat", "total", "group", "rule") VALUES ('12', '.docx', '4', '86', '0', '<?xml version="1.0" encoding="UTF-8" standalone="yes" ?>
<!DOCTYPE boost_serialization>
<boost_serialization signature="serialization::archive" version="13">
<dataObj class_id="0" tracking_level="0" version="0">
	<m_ruleType>1</m_ruleType>
	<m_qslPaths class_id="1" tracking_level="0" version="0">
		<stdList class_id="2" tracking_level="0" version="0">
			<count>7</count>
			<item_version>0</item_version>
			<item class_id="3" tracking_level="0" version="0">
				<stdString>C:\Users\Walkers\Desktop</stdString>
			</item>
			<item>
				<stdString>D:\SW_TestLog</stdString>
			</item>
			<item>
				<stdString>D:\SW_ThirdLibrarys</stdString>
			</item>
			<item>
				<stdString>E:\MyCode</stdString>
			</item>
			<item>
				<stdString>E:\MyIT</stdString>
			</item>
			<item>
				<stdString>E:\MySDK</stdString>
			</item>
			<item>
				<stdString>E:\MyWorkDir</stdString>
			</item>
		</stdList>
	</m_qslPaths>
</dataObj>
');
INSERT INTO "main"."IndexStat" ("id", "ext", "stat", "total", "group", "rule") VALUES ('13', '.pptx', '4', '356', '0', '<?xml version="1.0" encoding="UTF-8" standalone="yes" ?>
<!DOCTYPE boost_serialization>
<boost_serialization signature="serialization::archive" version="13">
<dataObj class_id="0" tracking_level="0" version="0">
	<m_ruleType>1</m_ruleType>
	<m_qslPaths class_id="1" tracking_level="0" version="0">
		<stdList class_id="2" tracking_level="0" version="0">
			<count>7</count>
			<item_version>0</item_version>
			<item class_id="3" tracking_level="0" version="0">
				<stdString>C:\Users\Walkers\Desktop</stdString>
			</item>
			<item>
				<stdString>D:\SW_TestLog</stdString>
			</item>
			<item>
				<stdString>D:\SW_ThirdLibrarys</stdString>
			</item>
			<item>
				<stdString>E:\MyCode</stdString>
			</item>
			<item>
				<stdString>E:\MyIT</stdString>
			</item>
			<item>
				<stdString>E:\MySDK</stdString>
			</item>
			<item>
				<stdString>E:\MyWorkDir</stdString>
			</item>
		</stdList>
	</m_qslPaths>
</dataObj>
');
INSERT INTO "main"."IndexStat" ("id", "ext", "stat", "total", "group", "rule") VALUES ('14', '.xlsx', '4', '454', '0', '<?xml version="1.0" encoding="UTF-8" standalone="yes" ?>
<!DOCTYPE boost_serialization>
<boost_serialization signature="serialization::archive" version="13">
<dataObj class_id="0" tracking_level="0" version="0">
	<m_ruleType>1</m_ruleType>
	<m_qslPaths class_id="1" tracking_level="0" version="0">
		<stdList class_id="2" tracking_level="0" version="0">
			<count>7</count>
			<item_version>0</item_version>
			<item class_id="3" tracking_level="0" version="0">
				<stdString>C:\Users\Walkers\Desktop</stdString>
			</item>
			<item>
				<stdString>D:\SW_TestLog</stdString>
			</item>
			<item>
				<stdString>D:\SW_ThirdLibrarys</stdString>
			</item>
			<item>
				<stdString>E:\MyCode</stdString>
			</item>
			<item>
				<stdString>E:\MyIT</stdString>
			</item>
			<item>
				<stdString>E:\MySDK</stdString>
			</item>
			<item>
				<stdString>E:\MyWorkDir</stdString>
			</item>
		</stdList>
	</m_qslPaths>
</dataObj>
');
INSERT INTO "main"."IndexStat" ("id", "ext", "stat", "total", "group", "rule") VALUES ('15', '.one', '4', '0', '0', '<?xml version="1.0" encoding="UTF-8" standalone="yes" ?>
<!DOCTYPE boost_serialization>
<boost_serialization signature="serialization::archive" version="13">
<dataObj class_id="0" tracking_level="0" version="0">
	<m_ruleType>1</m_ruleType>
	<m_qslPaths class_id="1" tracking_level="0" version="0">
		<stdList class_id="2" tracking_level="0" version="0">
			<count>7</count>
			<item_version>0</item_version>
			<item class_id="3" tracking_level="0" version="0">
				<stdString>C:\Users\Walkers\Desktop</stdString>
			</item>
			<item>
				<stdString>D:\SW_TestLog</stdString>
			</item>
			<item>
				<stdString>D:\SW_ThirdLibrarys</stdString>
			</item>
			<item>
				<stdString>E:\MyCode</stdString>
			</item>
			<item>
				<stdString>E:\MyIT</stdString>
			</item>
			<item>
				<stdString>E:\MySDK</stdString>
			</item>
			<item>
				<stdString>E:\MyWorkDir</stdString>
			</item>
		</stdList>
	</m_qslPaths>
</dataObj>
');
INSERT INTO "main"."IndexStat" ("id", "ext", "stat", "total", "group", "rule") VALUES ('16', '.txt', '4', '5075', '0', '<?xml version="1.0" encoding="UTF-8" standalone="yes" ?>
<!DOCTYPE boost_serialization>
<boost_serialization signature="serialization::archive" version="13">
<dataObj class_id="0" tracking_level="0" version="0">
	<m_ruleType>1</m_ruleType>
	<m_qslPaths class_id="1" tracking_level="0" version="0">
		<stdList class_id="2" tracking_level="0" version="0">
			<count>7</count>
			<item_version>0</item_version>
			<item class_id="3" tracking_level="0" version="0">
				<stdString>C:\Users\Walkers\Desktop</stdString>
			</item>
			<item>
				<stdString>D:\SW_TestLog</stdString>
			</item>
			<item>
				<stdString>D:\SW_ThirdLibrarys</stdString>
			</item>
			<item>
				<stdString>E:\MyCode</stdString>
			</item>
			<item>
				<stdString>E:\MyIT</stdString>
			</item>
			<item>
				<stdString>E:\MySDK</stdString>
			</item>
			<item>
				<stdString>E:\MyWorkDir</stdString>
			</item>
		</stdList>
	</m_qslPaths>
</dataObj>
');
INSERT INTO "main"."IndexStat" ("id", "ext", "stat", "total", "group", "rule") VALUES ('17', '.bat', '4', '474', '0', '<?xml version="1.0" encoding="UTF-8" standalone="yes" ?>
<!DOCTYPE boost_serialization>
<boost_serialization signature="serialization::archive" version="13">
<dataObj class_id="0" tracking_level="0" version="0">
	<m_ruleType>1</m_ruleType>
	<m_qslPaths class_id="1" tracking_level="0" version="0">
		<stdList class_id="2" tracking_level="0" version="0">
			<count>7</count>
			<item_version>0</item_version>
			<item class_id="3" tracking_level="0" version="0">
				<stdString>C:\Users\Walkers\Desktop</stdString>
			</item>
			<item>
				<stdString>D:\SW_TestLog</stdString>
			</item>
			<item>
				<stdString>D:\SW_ThirdLibrarys</stdString>
			</item>
			<item>
				<stdString>E:\MyCode</stdString>
			</item>
			<item>
				<stdString>E:\MyIT</stdString>
			</item>
			<item>
				<stdString>E:\MySDK</stdString>
			</item>
			<item>
				<stdString>E:\MyWorkDir</stdString>
			</item>
		</stdList>
	</m_qslPaths>
</dataObj>
');
INSERT INTO "main"."IndexStat" ("id", "ext", "stat", "total", "group", "rule") VALUES ('18', '.c', '4', '7252', '0', '<?xml version="1.0" encoding="UTF-8" standalone="yes" ?>
<!DOCTYPE boost_serialization>
<boost_serialization signature="serialization::archive" version="13">
<dataObj class_id="0" tracking_level="0" version="0">
	<m_ruleType>1</m_ruleType>
	<m_qslPaths class_id="1" tracking_level="0" version="0">
		<stdList class_id="2" tracking_level="0" version="0">
			<count>7</count>
			<item_version>0</item_version>
			<item class_id="3" tracking_level="0" version="0">
				<stdString>C:\Users\Walkers\Desktop</stdString>
			</item>
			<item>
				<stdString>D:\SW_TestLog</stdString>
			</item>
			<item>
				<stdString>D:\SW_ThirdLibrarys</stdString>
			</item>
			<item>
				<stdString>E:\MyCode</stdString>
			</item>
			<item>
				<stdString>E:\MyIT</stdString>
			</item>
			<item>
				<stdString>E:\MySDK</stdString>
			</item>
			<item>
				<stdString>E:\MyWorkDir</stdString>
			</item>
		</stdList>
	</m_qslPaths>
</dataObj>
');
INSERT INTO "main"."IndexStat" ("id", "ext", "stat", "total", "group", "rule") VALUES ('19', '.cpp', '4', '7581', '0', '<?xml version="1.0" encoding="UTF-8" standalone="yes" ?>
<!DOCTYPE boost_serialization>
<boost_serialization signature="serialization::archive" version="13">
<dataObj class_id="0" tracking_level="0" version="0">
	<m_ruleType>1</m_ruleType>
	<m_qslPaths class_id="1" tracking_level="0" version="0">
		<stdList class_id="2" tracking_level="0" version="0">
			<count>7</count>
			<item_version>0</item_version>
			<item class_id="3" tracking_level="0" version="0">
				<stdString>C:\Users\Walkers\Desktop</stdString>
			</item>
			<item>
				<stdString>D:\SW_TestLog</stdString>
			</item>
			<item>
				<stdString>D:\SW_ThirdLibrarys</stdString>
			</item>
			<item>
				<stdString>E:\MyCode</stdString>
			</item>
			<item>
				<stdString>E:\MyIT</stdString>
			</item>
			<item>
				<stdString>E:\MySDK</stdString>
			</item>
			<item>
				<stdString>E:\MyWorkDir</stdString>
			</item>
		</stdList>
	</m_qslPaths>
</dataObj>
');
INSERT INTO "main"."IndexStat" ("id", "ext", "stat", "total", "group", "rule") VALUES ('20', '.def', '4', '101', '0', '<?xml version="1.0" encoding="UTF-8" standalone="yes" ?>
<!DOCTYPE boost_serialization>
<boost_serialization signature="serialization::archive" version="13">
<dataObj class_id="0" tracking_level="0" version="0">
	<m_ruleType>1</m_ruleType>
	<m_qslPaths class_id="1" tracking_level="0" version="0">
		<stdList class_id="2" tracking_level="0" version="0">
			<count>7</count>
			<item_version>0</item_version>
			<item class_id="3" tracking_level="0" version="0">
				<stdString>C:\Users\Walkers\Desktop</stdString>
			</item>
			<item>
				<stdString>D:\SW_TestLog</stdString>
			</item>
			<item>
				<stdString>D:\SW_ThirdLibrarys</stdString>
			</item>
			<item>
				<stdString>E:\MyCode</stdString>
			</item>
			<item>
				<stdString>E:\MyIT</stdString>
			</item>
			<item>
				<stdString>E:\MySDK</stdString>
			</item>
			<item>
				<stdString>E:\MyWorkDir</stdString>
			</item>
		</stdList>
	</m_qslPaths>
</dataObj>
');
INSERT INTO "main"."IndexStat" ("id", "ext", "stat", "total", "group", "rule") VALUES ('21', '.gradle', '4', '43', '0', '<?xml version="1.0" encoding="UTF-8" standalone="yes" ?>
<!DOCTYPE boost_serialization>
<boost_serialization signature="serialization::archive" version="13">
<dataObj class_id="0" tracking_level="0" version="0">
	<m_ruleType>1</m_ruleType>
	<m_qslPaths class_id="1" tracking_level="0" version="0">
		<stdList class_id="2" tracking_level="0" version="0">
			<count>7</count>
			<item_version>0</item_version>
			<item class_id="3" tracking_level="0" version="0">
				<stdString>C:\Users\Walkers\Desktop</stdString>
			</item>
			<item>
				<stdString>D:\SW_TestLog</stdString>
			</item>
			<item>
				<stdString>D:\SW_ThirdLibrarys</stdString>
			</item>
			<item>
				<stdString>E:\MyCode</stdString>
			</item>
			<item>
				<stdString>E:\MyIT</stdString>
			</item>
			<item>
				<stdString>E:\MySDK</stdString>
			</item>
			<item>
				<stdString>E:\MyWorkDir</stdString>
			</item>
		</stdList>
	</m_qslPaths>
</dataObj>
');
INSERT INTO "main"."IndexStat" ("id", "ext", "stat", "total", "group", "rule") VALUES ('22', '.h', '4', '17170', '0', '<?xml version="1.0" encoding="UTF-8" standalone="yes" ?>
<!DOCTYPE boost_serialization>
<boost_serialization signature="serialization::archive" version="13">
<dataObj class_id="0" tracking_level="0" version="0">
	<m_ruleType>1</m_ruleType>
	<m_qslPaths class_id="1" tracking_level="0" version="0">
		<stdList class_id="2" tracking_level="0" version="0">
			<count>7</count>
			<item_version>0</item_version>
			<item class_id="3" tracking_level="0" version="0">
				<stdString>C:\Users\Walkers\Desktop</stdString>
			</item>
			<item>
				<stdString>D:\SW_TestLog</stdString>
			</item>
			<item>
				<stdString>D:\SW_ThirdLibrarys</stdString>
			</item>
			<item>
				<stdString>E:\MyCode</stdString>
			</item>
			<item>
				<stdString>E:\MyIT</stdString>
			</item>
			<item>
				<stdString>E:\MySDK</stdString>
			</item>
			<item>
				<stdString>E:\MyWorkDir</stdString>
			</item>
		</stdList>
	</m_qslPaths>
</dataObj>
');
INSERT INTO "main"."IndexStat" ("id", "ext", "stat", "total", "group", "rule") VALUES ('23', '.ini', '4', '4687', '0', '<?xml version="1.0" encoding="UTF-8" standalone="yes" ?>
<!DOCTYPE boost_serialization>
<boost_serialization signature="serialization::archive" version="13">
<dataObj class_id="0" tracking_level="0" version="0">
	<m_ruleType>1</m_ruleType>
	<m_qslPaths class_id="1" tracking_level="0" version="0">
		<stdList class_id="2" tracking_level="0" version="0">
			<count>7</count>
			<item_version>0</item_version>
			<item class_id="3" tracking_level="0" version="0">
				<stdString>C:\Users\Walkers\Desktop</stdString>
			</item>
			<item>
				<stdString>D:\SW_TestLog</stdString>
			</item>
			<item>
				<stdString>D:\SW_ThirdLibrarys</stdString>
			</item>
			<item>
				<stdString>E:\MyCode</stdString>
			</item>
			<item>
				<stdString>E:\MyIT</stdString>
			</item>
			<item>
				<stdString>E:\MySDK</stdString>
			</item>
			<item>
				<stdString>E:\MyWorkDir</stdString>
			</item>
		</stdList>
	</m_qslPaths>
</dataObj>
');
INSERT INTO "main"."IndexStat" ("id", "ext", "stat", "total", "group", "rule") VALUES ('24', '.java', '4', '3240', '0', '<?xml version="1.0" encoding="UTF-8" standalone="yes" ?>
<!DOCTYPE boost_serialization>
<boost_serialization signature="serialization::archive" version="13">
<dataObj class_id="0" tracking_level="0" version="0">
	<m_ruleType>1</m_ruleType>
	<m_qslPaths class_id="1" tracking_level="0" version="0">
		<stdList class_id="2" tracking_level="0" version="0">
			<count>7</count>
			<item_version>0</item_version>
			<item class_id="3" tracking_level="0" version="0">
				<stdString>C:\Users\Walkers\Desktop</stdString>
			</item>
			<item>
				<stdString>D:\SW_TestLog</stdString>
			</item>
			<item>
				<stdString>D:\SW_ThirdLibrarys</stdString>
			</item>
			<item>
				<stdString>E:\MyCode</stdString>
			</item>
			<item>
				<stdString>E:\MyIT</stdString>
			</item>
			<item>
				<stdString>E:\MySDK</stdString>
			</item>
			<item>
				<stdString>E:\MyWorkDir</stdString>
			</item>
		</stdList>
	</m_qslPaths>
</dataObj>
');
INSERT INTO "main"."IndexStat" ("id", "ext", "stat", "total", "group", "rule") VALUES ('25', '.js', '4', '12327', '0', '<?xml version="1.0" encoding="UTF-8" standalone="yes" ?>
<!DOCTYPE boost_serialization>
<boost_serialization signature="serialization::archive" version="13">
<dataObj class_id="0" tracking_level="0" version="0">
	<m_ruleType>1</m_ruleType>
	<m_qslPaths class_id="1" tracking_level="0" version="0">
		<stdList class_id="2" tracking_level="0" version="0">
			<count>7</count>
			<item_version>0</item_version>
			<item class_id="3" tracking_level="0" version="0">
				<stdString>C:\Users\Walkers\Desktop</stdString>
			</item>
			<item>
				<stdString>D:\SW_TestLog</stdString>
			</item>
			<item>
				<stdString>D:\SW_ThirdLibrarys</stdString>
			</item>
			<item>
				<stdString>E:\MyCode</stdString>
			</item>
			<item>
				<stdString>E:\MyIT</stdString>
			</item>
			<item>
				<stdString>E:\MySDK</stdString>
			</item>
			<item>
				<stdString>E:\MyWorkDir</stdString>
			</item>
		</stdList>
	</m_qslPaths>
</dataObj>
');
INSERT INTO "main"."IndexStat" ("id", "ext", "stat", "total", "group", "rule") VALUES ('26', '.kt', '4', '655', '0', '<?xml version="1.0" encoding="UTF-8" standalone="yes" ?>
<!DOCTYPE boost_serialization>
<boost_serialization signature="serialization::archive" version="13">
<dataObj class_id="0" tracking_level="0" version="0">
	<m_ruleType>1</m_ruleType>
	<m_qslPaths class_id="1" tracking_level="0" version="0">
		<stdList class_id="2" tracking_level="0" version="0">
			<count>7</count>
			<item_version>0</item_version>
			<item class_id="3" tracking_level="0" version="0">
				<stdString>C:\Users\Walkers\Desktop</stdString>
			</item>
			<item>
				<stdString>D:\SW_TestLog</stdString>
			</item>
			<item>
				<stdString>D:\SW_ThirdLibrarys</stdString>
			</item>
			<item>
				<stdString>E:\MyCode</stdString>
			</item>
			<item>
				<stdString>E:\MyIT</stdString>
			</item>
			<item>
				<stdString>E:\MySDK</stdString>
			</item>
			<item>
				<stdString>E:\MyWorkDir</stdString>
			</item>
		</stdList>
	</m_qslPaths>
</dataObj>
');
INSERT INTO "main"."IndexStat" ("id", "ext", "stat", "total", "group", "rule") VALUES ('27', '.py', '4', '21404', '0', '<?xml version="1.0" encoding="UTF-8" standalone="yes" ?>
<!DOCTYPE boost_serialization>
<boost_serialization signature="serialization::archive" version="13">
<dataObj class_id="0" tracking_level="0" version="0">
	<m_ruleType>1</m_ruleType>
	<m_qslPaths class_id="1" tracking_level="0" version="0">
		<stdList class_id="2" tracking_level="0" version="0">
			<count>7</count>
			<item_version>0</item_version>
			<item class_id="3" tracking_level="0" version="0">
				<stdString>C:\Users\Walkers\Desktop</stdString>
			</item>
			<item>
				<stdString>D:\SW_TestLog</stdString>
			</item>
			<item>
				<stdString>D:\SW_ThirdLibrarys</stdString>
			</item>
			<item>
				<stdString>E:\MyCode</stdString>
			</item>
			<item>
				<stdString>E:\MyIT</stdString>
			</item>
			<item>
				<stdString>E:\MySDK</stdString>
			</item>
			<item>
				<stdString>E:\MyWorkDir</stdString>
			</item>
		</stdList>
	</m_qslPaths>
</dataObj>
');
INSERT INTO "main"."IndexStat" ("id", "ext", "stat", "total", "group", "rule") VALUES ('28', '.sh', '4', '181', '0', '<?xml version="1.0" encoding="UTF-8" standalone="yes" ?>
<!DOCTYPE boost_serialization>
<boost_serialization signature="serialization::archive" version="13">
<dataObj class_id="0" tracking_level="0" version="0">
	<m_ruleType>1</m_ruleType>
	<m_qslPaths class_id="1" tracking_level="0" version="0">
		<stdList class_id="2" tracking_level="0" version="0">
			<count>7</count>
			<item_version>0</item_version>
			<item class_id="3" tracking_level="0" version="0">
				<stdString>C:\Users\Walkers\Desktop</stdString>
			</item>
			<item>
				<stdString>D:\SW_TestLog</stdString>
			</item>
			<item>
				<stdString>D:\SW_ThirdLibrarys</stdString>
			</item>
			<item>
				<stdString>E:\MyCode</stdString>
			</item>
			<item>
				<stdString>E:\MyIT</stdString>
			</item>
			<item>
				<stdString>E:\MySDK</stdString>
			</item>
			<item>
				<stdString>E:\MyWorkDir</stdString>
			</item>
		</stdList>
	</m_qslPaths>
</dataObj>
');
INSERT INTO "main"."IndexStat" ("id", "ext", "stat", "total", "group", "rule") VALUES ('31', '.csv', '4', '181', '0', '<?xml version="1.0" encoding="UTF-8" standalone="yes" ?>
<!DOCTYPE boost_serialization>
<boost_serialization signature="serialization::archive" version="13">
<dataObj class_id="0" tracking_level="0" version="0">
	<m_ruleType>1</m_ruleType>
	<m_qslPaths class_id="1" tracking_level="0" version="0">
		<stdList class_id="2" tracking_level="0" version="0">
			<count>7</count>
			<item_version>0</item_version>
			<item class_id="3" tracking_level="0" version="0">
				<stdString>C:\Users\Walkers\Desktop</stdString>
			</item>
			<item>
				<stdString>D:\SW_TestLog</stdString>
			</item>
			<item>
				<stdString>D:\SW_ThirdLibrarys</stdString>
			</item>
			<item>
				<stdString>E:\MyCode</stdString>
			</item>
			<item>
				<stdString>E:\MyIT</stdString>
			</item>
			<item>
				<stdString>E:\MySDK</stdString>
			</item>
			<item>
				<stdString>E:\MyWorkDir</stdString>
			</item>
		</stdList>
	</m_qslPaths>
</dataObj>
');
```