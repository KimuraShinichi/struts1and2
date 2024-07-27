<%@ taglib uri="http://struts.apache.org/tags-bean" prefix="bean" %>
<%@ taglib uri="http://struts.apache.org/tags-html" prefix="html" %>
<%@ taglib uri="http://struts.apache.org/tags-logic" prefix="logic" %>
<%@ page contentType="text/html; charset=UTF-8" %>
<%@ page pageEncoding="UTF-8" %>

<html:html>
<head>
    <title>Welcome Page</title>
</head>
<body>
    <html:form action="/login" method="post">
        <table>
            <tr>
                <td>ようこそ</td>
            </tr>
        </table>
    </html:form>
</body>
</html:html>
