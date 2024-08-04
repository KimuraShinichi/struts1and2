function collect_errors() {
    // HTML内の全ての span.errorMessage 要素を取得します
    const errorMessages = document.querySelectorAll('span.errorMessage');
    
    // 既存の error-header 要素を取得します
    const errorHeader = document.querySelector('div.error-header');
    
    // 各 errorMessage 要素を処理して p.error 要素に変換して errorHeader に追加します
    errorMessages.forEach((errorMessage) => {
        const errorParagraph = document.createElement('p');
        errorParagraph.classList.add('error');
        errorParagraph.textContent = errorMessage.textContent;
        errorHeader.appendChild(errorParagraph);
    });
}
function do_collect_errors() {
    document.addEventListener('DOMContentLoaded', function() {
        collect_errors();
    });
}
