<%-----------------------------------------------------------------------
 - エラー画面
 - ファイル名 : N000Error.jsp
 - 説明       : エラー画面を表示します。
 -
 - $LastChangedRevision: 37352 $
 - $LastChangedDate:: 2022-06-02 16:49:48#$
 -----------------------------------------------------------------------%>

<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd"> 
<%@ page contentType="text/html; charset=Windows-31J" %>
<%@ taglib uri="/WEB-INF/tld/struts-html.tld"    prefix="html" %>
<%@ taglib uri="/WEB-INF/tld/struts-bean.tld"    prefix="bean" %>
<%
	// コンテキストルートを取得
	String contextPath = request.getContextPath();
%>

<%-- CSSの読み込み --%>
<link rel="stylesheet" type="text/css" href="<%=contextPath%>/css/N000Common.css"/>

<html:html>
<head>
  <meta http-equiv="Content-Type" content="text/html charset=Shift_JIS"/>
  <meta http-equiv="Content-Script-Type" content="text/javascript"/>
   
<title><bean:message key="title.err"/></title>
       
</head>

<%-- 背景をピンクにする --%>
<body id="error">
	<%-- N000Message.jspの呼出し --%>
 	<div><jsp:include page="N000Message.jsp"/></div>

</body>
</html:html>