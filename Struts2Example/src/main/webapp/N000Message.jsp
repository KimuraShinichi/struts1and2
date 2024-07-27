<%@ page contentType="text/html; charset=Windows-31J" %>
<%@ taglib prefix="s" uri="/struts-tags" %>

    <s:if test="hasActionMessages()">
        <s:text name="messages.header"/>
        <s:iterator value="actionMessages">
            <s:text name="messages.prefix"/>
            <s:property/>
            <s:text name="messages.suffix"/>
        </s:iterator>
        <s:text name="messages.footer"/>
    </s:if>
    
    <s:if test="hasActionErrors()">
        <s:text name="errors.header"/>
        <s:iterator value="actionErrors">
            <s:text name="errors.prefix"/>
            <s:property/>
            <s:text name="errors.suffix"/>
        </s:iterator>
        <s:text name="errors.footer"/>
    </s:if>
