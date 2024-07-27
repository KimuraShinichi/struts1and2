package com.example.web;

import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import org.apache.struts.action.Action;
import org.apache.struts.action.ActionForm;
import org.apache.struts.action.ActionForward;
import org.apache.struts.action.ActionMapping;
import org.apache.struts.action.ActionMessages;
import org.apache.struts.action.ActionMessage;

public class ShowMessageAction extends Action {
    public ActionForward execute(ActionMapping mapping, ActionForm form, HttpServletRequest request, HttpServletResponse response) {
        
        // サンプルメッセージの追加
        ActionMessages messages = new ActionMessages();
        messages.add(ActionMessages.GLOBAL_MESSAGE, new ActionMessage("message.success", "操作が成功しました。"));

        ActionMessages errors = new ActionMessages();
        errors.add(ActionMessages.GLOBAL_MESSAGE, new ActionMessage("message.error", "エラーが発生しました。"));

        saveMessages(request, messages);
        saveErrors(request, errors);

        return mapping.findForward("success");
    }
}
