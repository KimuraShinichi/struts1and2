<%@ taglib uri="/WEB-INF/tld/struts-bean.tld" prefix="bean" %>
<%@ taglib uri="/WEB-INF/tld/struts-html.tld" prefix="html" %>
<%@ taglib uri="/WEB-INF/tld/struts-logic.tld" prefix="logic" %>
<%@ page contentType="text/html; charset=UTF-8" %>
<%@ page pageEncoding="UTF-8" %>
<%@ page import="javax.servlet.http.HttpServletRequest" %>

<html:html>
<head>
    <title><bean:message key="login.title"/></title>
</head>
<body>
    <html:form action="/login" method="post">
        <%-- GETメソッドで初期表示の場合は入力が空値でもエラー表示しない。 --%>
        <% if ("POST".equals(request.getMethod())) { %><html:errors/><% } %>
        <table>
            <tr>
                <td><bean:message key="login.label.userId"/></td>
                <td><html:text property="userId"/></td>
            </tr>
            <tr>
                <td><bean:message key="login.label.password"/></td>
                <td><html:password property="password"/></td>
            </tr>
            <tr>
                <td colspan="2">
                    <html:submit property="submitButton">
                        <bean:message key='login.button.submit'/>
                    </html:submit>
                </td>
            </tr>
        </table>
    </html:form>
</body>
</html:html>
