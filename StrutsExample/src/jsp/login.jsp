<%@ taglib uri="http://struts.apache.org/tags-bean" prefix="bean" %>
<%@ taglib uri="http://struts.apache.org/tags-html" prefix="html" %>
<%@ taglib uri="http://struts.apache.org/tags-logic" prefix="logic" %>
<%@ page contentType="text/html; charset=UTF-8" %>
<%@ page pageEncoding="UTF-8" %>

<html:html>
<head>
    <title>Login Page</title>
</head>
<body>
    <html:form action="/login" method="post">
        <table>
            <tr>
                <td><html:errors property="username"/></td>
            </tr>
            <tr>
                <td>Username:</td>
                <td><html:text property="username"/></td>
            </tr>
            <tr>
                <td><html:errors property="password"/></td>
            </tr>
            <tr>
                <td>Password:</td>
                <td><html:password property="password"/></td>
            </tr>
            <tr>
                <td colspan="2"><html:submit value="Login"/></td>
            </tr>
        </table>
    </html:form>
</body>
</html:html>
