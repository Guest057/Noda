function showSection(sectionNumber) {
    document.querySelectorAll('.tab').forEach(tab => tab.classList.remove('active'));
    document.querySelectorAll('.content').forEach(content => content.classList.remove('active'));

    document.querySelector('.tab:nth-child(' + sectionNumber + ')').classList.add('active');
    document.getElementById('section' + sectionNumber).classList.add('active');
}