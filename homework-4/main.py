from src.video import Video, PLVideo

if __name__ == '__main__':
    # Создаем два экземпляра класса
    video1 = Video('udsgzdZw5zU')  # 'udsgzdZw5zU' - это id видео из ютуб
    video2 = PLVideo('udsgzdZw5zU', 'PLv_zOGKKxVph_8g2Mqc3LMhj0M_BfasbC')
    assert str(video1) == 'Сергей Орлов vs SQWOZ BAB - Кто заберёт ФЕРРАРИ? 5 выпуск'
    assert str(video2) == 'Сергей Орлов vs SQWOZ BAB - Кто заберёт ФЕРРАРИ? 5 выпуск'
