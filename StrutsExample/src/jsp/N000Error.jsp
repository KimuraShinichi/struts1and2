<%-----------------------------------------------------------------------
 - �G���[���
 - �t�@�C���� : N000Error.jsp
 - ����       : �G���[��ʂ�\�����܂��B
 -
 - $LastChangedRevision: 37352 $
 - $LastChangedDate:: 2022-06-02 16:49:48#$
 -----------------------------------------------------------------------%>

<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd"> 
<%@ page contentType="text/html; charset=Windows-31J" %>
<%@ taglib uri="/WEB-INF/tld/struts-html.tld"    prefix="html" %>
<%@ taglib uri="/WEB-INF/tld/struts-bean.tld"    prefix="bean" %>
<%
	// �R���e�L�X�g���[�g���擾
	String contextPath = request.getContextPath();
%>

<%-- CSS�̓ǂݍ��� --%>
<link rel="stylesheet" type="text/css" href="<%=contextPath%>/css/N000Common.css"/>

<html:html>
<head>
  <meta http-equiv="Content-Type" content="text/html charset=Shift_JIS"/>
  <meta http-equiv="Content-Script-Type" content="text/javascript"/>
   
<title><bean:message key="title.err"/></title>
       
</head>

<%-- �w�i���s���N�ɂ��� --%>
<body id="error">
	<%-- N000Message.jsp�̌ďo�� --%>
 	<div><jsp:include page="N000Message.jsp"/></div>

</body>
</html:html>