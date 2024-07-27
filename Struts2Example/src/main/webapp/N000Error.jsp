<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<%@ page contentType="text/html; charset=Windows-31J" %>
<%@ taglib prefix="s" uri="/struts-tags" %>
<%
    // コンテキストルートを取得
    String contextPath = request.getContextPath();
%>

<%-- CSSの読み込み --%>
<link rel="stylesheet" type="text/css" href="<%=contextPath%>/css/N000Common.css"/>

<html>
<head>
    <meta http-equiv="Content-Type" content="text/html; charset=Shift_JIS"/>
    <meta http-equiv="Content-Script-Type" content="text/javascript"/>
    <title><s:text name="title.err"/></title>
</head>

<%-- 背景をピンクにする --%>
<body id="error">
    <%-- N000Message.jspの呼出し --%>
    <div><jsp:include page="N000Message.jsp"/></div>
</body>
</html>
