<%-----------------------------------------------------------------------
 - 共通メッセージ(成功/エラー)
 - ファイル名 : N000Common.jsp
 - 説明       : 共通メッセージ画面を表示します。
 -
 - $LastChangedRevision: 37352 $
 - $LastChangedDate:: 2022-06-02 16:49:48#$
 -----------------------------------------------------------------------%>
<%@ page contentType="text/html; charset=Windows-31J" %>
<%@ taglib uri="/WEB-INF/tld/struts-html.tld"  prefix="html" %>
<%@ taglib uri="/WEB-INF/tld/struts-bean.tld"  prefix="bean" %>

<%-- 処理結果：成功メッセージ表示 --%>    
<html:messages id="msg" message="true" header="messages.header" footer="messages.footer">
  <bean:message key="messages.prefix" />
  <bean:write name="msg" />
  <bean:message key="messages.suffix" />
</html:messages>

<%-- 処理結果：エラーメッセージ表示 --%>    
<html:messages id="err" message="false" header="errors.header" footer="errors.footer">
  <bean:message key="errors.prefix" />
  <bean:write name="err" />
  <bean:message key="errors.suffix" />
</html:messages>
