<%-----------------------------------------------------------------------
 - ���ʃ��b�Z�[�W(����/�G���[)
 - �t�@�C���� : N000Common.jsp
 - ����       : ���ʃ��b�Z�[�W��ʂ�\�����܂��B
 -
 - $LastChangedRevision: 37352 $
 - $LastChangedDate:: 2022-06-02 16:49:48#$
 -----------------------------------------------------------------------%>
<%@ page contentType="text/html; charset=Windows-31J" %>
<%@ taglib uri="/WEB-INF/tld/struts-html.tld"  prefix="html" %>
<%@ taglib uri="/WEB-INF/tld/struts-bean.tld"  prefix="bean" %>

<%-- �������ʁF�������b�Z�[�W�\�� --%>    
<html:messages id="msg" message="true" header="messages.header" footer="messages.footer">
  <bean:message key="messages.prefix" />
  <bean:write name="msg" />
  <bean:message key="messages.suffix" />
</html:messages>

<%-- �������ʁF�G���[���b�Z�[�W�\�� --%>    
<html:messages id="err" message="false" header="errors.header" footer="errors.footer">
  <bean:message key="errors.prefix" />
  <bean:write name="err" />
  <bean:message key="errors.suffix" />
</html:messages>
