package com.example.web.action;

import org.apache.logging.log4j.LogManager;
import org.apache.logging.log4j.Logger;

import java.util.Map;
import java.util.List;
import java.util.stream.IntStream;

import com.opensymphony.xwork2.ActionSupport;

import com.opensymphony.xwork2.validator.annotations.RequiredStringValidator;
import com.opensymphony.xwork2.validator.annotations.StringLengthFieldValidator;
import com.opensymphony.xwork2.validator.annotations.Validations;

@Validations(
    requiredStrings = {
        @RequiredStringValidator(fieldName = "userId", key = "errors.required", shortCircuit=true)
    },
    stringLengthFields = {
        @StringLengthFieldValidator(fieldName = "userId", minLength = "2", key = "errors.minlength", shortCircuit=true),
        @StringLengthFieldValidator(fieldName = "userId", maxLength = "12", key = "errors.maxlength", shortCircuit=true),
        @StringLengthFieldValidator(fieldName = "password", minLength = "0", key = "errors.minlength", shortCircuit=true),
        @StringLengthFieldValidator(fieldName = "password", maxLength = "24", key = "errors.maxlength", shortCircuit=true)
    }
)
public class LoginAction extends ActionSupport {
    private static final Logger logger = LogManager.getLogger(LoginAction.class);

    private String userId;
    private String password;

    public String getUserId() { return this.userId; }
    public void setUserId(String userId) { this.userId = userId; }

    public String getPassword() { return this.password; }
    public void setPassword(String password) { this.password = password; }

    @Override
    public void validate() {
        // フィールドエラーを確認し、プレースホルダーがあればパラメータで置換する。
        logger.info("Converting error messages.");
        convertFieldErrors("userId", new String[]{getText("login.name.userId"), "2(最小値)", "12(最大値)"});
        convertFieldErrors("password", new String[]{getText("login.name.password"), "0(最小値)", "24(最大値)"});
    }

    @Override
    public String execute() {
        logger.info("userId=" + userId + ";");
        logger.info("password=" + password + ";");

        if (!this.certify(userId, password)) {
            logger.info("Failed to certificate;");

            addFieldError("userId", getText("login.error"));
            return ActionSupport.INPUT;
        }

        logger.info("Success to certificate;");
        return ActionSupport.SUCCESS;
    }

    protected boolean certify(String userId, String password) {
        return ("admin".equals(userId) && "admin".equals(password));
    }

    /**
     * フォーム項目についてのエラーメッセージに含まれるプレースホルダー（{0}等）をパラメータ文字列の配列要素で置換する。
     *
     * @param fieldName - フォーム項目名（HTML の input 要素の name 属性値）。
     * @param params - メッセージ中のプレースホルダーを置換するためのパラメータ文字列の配列。
     */
    protected void convertFieldErrors(String fieldName, String[] params) {
        logger.info("実行: convertFieldErrors[fieldName='" + fieldName + "]");
        Map<String, List<String>> fieldErrors = getFieldErrors();
        List<String> errors = fieldErrors.get(fieldName);
        logger.info("errors=" + errors + "");
        if (errors != null && !errors.isEmpty()) {
            int messageSize = errors.size();
            logger.info("messageSize=" + messageSize + "");
            for (int messageIndex = 0; messageIndex < messageSize; ++messageIndex) {
                String error = errors.get(messageIndex);
                error = applyParamsOntoPlaceHolders(error, params);
                errors.set(messageIndex, error);
            }
        }
    }

    /**
     * メッセージ文字列の中にプレースホルダー文字列（{0}, {1} 等）があればパラメータ文字列で置換してその結果の文字列を返す。
     *
     * プレースホルダー文字列 {i} をパラメータ文字列 params[i] で置換する。
     * パラメータ文字列 params[] の要素数を超える番号のプレースホルダーは無視する。
     *
     * メッセージ中のプレースホルダー番号({0}における0等)に途中未使用の整数があってもよい。
     *     String converted = applyParamsOntoPlaceHolders("{0}-{2}", new String[]{"あ", "い", "う"}, 0, 10);
     * 上記の場合、{2} が未使用だが、"あ" → {0}, "う" → {2} のように対応して置換する。
     *     converted == "あ-う"
     *
     * @param message - メッセージ文字列。
     * @param params  - パラメータ文字列の配列。
     * @return 適宜変更されたメッセージ文字列。
     */
    protected String applyParamsOntoPlaceHolders(String message, String[] params) {
        for (int paramIndex = 0; paramIndex < params.length; ++paramIndex) {
            int holderNumber = paramIndex;
            String placeHolder = "{" + holderNumber + "}";
            String paramValue = params[paramIndex];
            if (!message.contains(placeHolder)) {
                continue;
            }
            logger.info("Replacing '" + message + "' with ['" + placeHolder + "' <-- '" + paramValue + "']");
            message = message.replace(placeHolder, paramValue);
        }
        return message;
    }
}
