// Кастомный JavaScript для админки BanaBlack
document.addEventListener('DOMContentLoaded', function() {
    // Добавляем кастомные функции здесь
    console.log('BanaBlack Admin loaded');

    // Пример: добавляем подтверждение для опасных действий
    const deleteButtons = document.querySelectorAll('.deletelink');
    deleteButtons.forEach(button => {
        button.addEventListener('click', function(e) {
            if (!confirm('Вы уверены, что хотите удалить этот объект?')) {
                e.preventDefault();
            }
        });
    });
});