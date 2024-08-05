<%@ taglib uri="/WEB-INF/tld/struts-bean.tld" prefix="bean" %>
<%@ taglib uri="/WEB-INF/tld/struts-html.tld" prefix="html" %>
<%@ taglib uri="/WEB-INF/tld/struts-logic.tld" prefix="logic" %>
<%@ page contentType="text/html; charset=UTF-8" %>
<%@ page pageEncoding="UTF-8" %>
<%@ page import="javax.servlet.http.HttpServletRequest" %>

<html:html>
<head>
    <title><bean:message key="profile.title"/></title>
</head>
<body>
    <h2><bean:message key="profile.title"/></h2>

    <html:form action="/profile.do" method="post">
        <%-- GETメソッドで初期表示の場合は入力が空値でもエラー表示しない。 --%>
        <% if ("POST".equals(request.getMethod())) { %><html:errors/><% } %>
        <div>
            <label for="firstName"><bean:message key="profile.name.firstName"/>:</label>
            <html:text property="firstName" size="20" maxlength="50"/>
        </div>
        <div>
            <label for="lastName"><bean:message key="profile.name.lastName"/>:</label>
            <html:text property="lastName" size="20" maxlength="50"/>
        </div>
        <div>
            <label for="email"><bean:message key="profile.name.email"/>:</label>
            <html:text property="email" size="30" maxlength="100"/>
        </div>
        <div>
            <label for="age"><bean:message key="profile.name.age"/>:</label>
            <html:text property="age" size="3" maxlength="3"/>
        </div>
        <div>
            <label><bean:message key="profile.name.gender"/>:</label>
            <html:radio property="gender" value="male" title="Male" /> Male
            <html:radio property="gender" value="female" title="Female" /> Female
            <html:radio property="gender" value="other" title="Other" /> Other
        </div>
        <div>
            <label for="bio"><bean:message key="profile.name.bio"/>:</label>
            <html:textarea property="bio" rows="4" cols="50"/>
        </div>
        <div>
            <label>
                <html:checkbox property="agree"/><bean:message key="profile.name.agree"/>
            </label>
        </div>
        <div>
             <html:submit>
                 <bean:message key='profile.button.submit'/>
             </html:submit>
        </div>
    </html:form>
</body>
</html:html>
