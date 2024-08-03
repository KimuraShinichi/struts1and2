<%@ taglib uri="/struts-tags" prefix="s" %>
<%@ page contentType="text/html; charset=UTF-8" %>
<%@ page pageEncoding="UTF-8" %>
<!--%@ page import="javax.servlet.http.HttpServletRequest" %-->

<html>
<head>
    <title><s:text name="login.title"/></title>
    <%-- GETメソッドで初期表示の場合は入力が空値でもエラー表示しない。 --%>
    <% if ("GET".equals(request.getMethod())) { %>
        <link rel="stylesheet" type="text/css" href="<%=request.getContextPath()%>/css/unable_field_error.css">
    <% } %>
</head>
<body>
    <s:form action="login" method="post">
        <table>
            <tr>
                <td></td>
                <td><s:textfield name="userId" key="login.label.userId"/></td>
            </tr>
            <tr>
                <td></td>
                <td><s:password name="password" key="login.label.password"/></td>
            </tr>
            <tr>
                <td colspan="2">
                    <s:submit value="%{getText('login.button.submit')}" />
                </td>
            </tr>
        </table>
    </s:form>
</body>
</html>
