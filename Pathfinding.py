import pygame
import sys

from board import Board
from constants import *
# If you're reading this, I think you're cute <3
pygame.init()
clock = pygame.time.Clock()


def menu():
    global clock
    # BACKGROUND
    imp = pygame.image.load("PIC2.jpg")
    screen.blit(imp, (0, 0))
    pygame.display.flip()
    # BUTTONS
    dfs_rect = pygame.Rect((WIDTH // 2 - WIDTH // 3, 2 * HEIGHT // 3 - HEIGHT // 12), (WIDTH // 6, HEIGHT // 6))
    pygame.draw.rect(screen, BUTTON1_COLOR, dfs_rect, 5, 15)
    bfs_rect = pygame.Rect((WIDTH // 2 - WIDTH // 12, 2 * HEIGHT // 3 - HEIGHT // 12), (WIDTH // 6, HEIGHT // 6))
    pygame.draw.rect(screen, BUTTON2_COLOR, bfs_rect, 5, 15)
    a_start_rect = pygame.Rect((WIDTH // 2 + WIDTH // 6, 2 * HEIGHT // 3 - HEIGHT // 12), (WIDTH // 6, HEIGHT // 6))
    pygame.draw.rect(screen, BUTTON3_COLOR, a_start_rect, 5, 15)
    # TEXT FOR BUTTONS
    Cambria = pygame.font.SysFont("verdana", 40)

    dfs_text = Cambria.render("dFirstS", True, 'White')
    dfs_surf = dfs_text.get_rect(center=(WIDTH // 2 - WIDTH // 4, 2 * HEIGHT // 3))
    screen.blit(dfs_text, dfs_surf)

    bfs_text = Cambria.render("bFirstS", True, "White")
    bfs_surf = dfs_text.get_rect(center=(WIDTH // 2, 2 * HEIGHT // 3))
    screen.blit(bfs_text, bfs_surf)

    astar_text = Cambria.render("aStar", True, "White")
    astar_surf = astar_text.get_rect(center=(WIDTH // 2 + WIDTH // 4, 2 * HEIGHT // 3))
    screen.blit(astar_text, astar_surf)
    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEMOTION:
                mouse_pos = pygame.mouse.get_pos()
                if dfs_rect.collidepoint(mouse_pos) or bfs_rect.collidepoint(mouse_pos) or a_start_rect.collidepoint(
                        mouse_pos):
                    pygame.mouse.set_cursor(pygame.cursors.Cursor(pygame.SYSTEM_CURSOR_HAND))
                else:
                    pygame.mouse.set_cursor(pygame.cursors.Cursor(pygame.SYSTEM_CURSOR_ARROW))
            if event.type == pygame.MOUSEBUTTONUP:
                if dfs_rect.collidepoint(pygame.mouse.get_pos()): return 0
                if bfs_rect.collidepoint(pygame.mouse.get_pos()): return 1
                if a_start_rect.collidepoint(pygame.mouse.get_pos()): return 2
        pygame.display.set_caption("Find_the_Flag! - FPS: %.0f" % clock.get_fps())
        clock.tick(FPS)

def main():
    global screen, algo_is_showing
    screen = pygame.display.set_mode(SIZE_OF_DISPLAY)
    pygame.display.init()
    chosen = menu()
    screen.fill(WHITE)
    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_WAIT)
    b = Board(screen, 64, 64)
    b.all_squares(instant=True)
    dragging, start, end = False, True, True
    placing, algo_is_showing, dragging_for_walls = False, False, False
    pygame.mouse.set_cursor(pygame.cursors.Cursor(pygame.SYSTEM_CURSOR_ARROW))
    while True:
        b.all_squares(instant=True)
        screen.fill(WHITE)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_CAPSLOCK:
                    placing = not placing
                if event.key == pygame.K_ESCAPE:
                    b.reset_marks()
                    dragging, start, end = False, True, True
                    placing, algo_is_showing = False, False
                    chosen = menu()
                if event.key == pygame.K_SPACE:
                    if not algo_is_showing:
                        if chosen == 0:
                            b.dfs_graphics()
                        elif chosen == 1:
                            b.bfs_graphics()
                        else:
                            b.a_star_graphics()
                        algo_is_showing = True
                    else:
                        b.reset_marks()
                        algo_is_showing = False
            if event.type == pygame.MOUSEBUTTONDOWN and not placing:
                if event.button == 2: dragging = True
                elif event.button == 4: b.zoom_in()
                elif event.button == 5: b.zoom_out()
            elif event.type == pygame.MOUSEMOTION:
                shift = pygame.mouse.get_rel()
                if dragging: b.move(shift)
            elif event.type == pygame.MOUSEBUTTONUP and not placing:
                dragging = False
                if event.button == 1 and start:
                    x, y = pygame.mouse.get_pos()
                    cord = b.collide_point(x, y)
                    if cord[0] and cord[1] is not None:
                        b.grid[cord[1]][cord[2]].mark_cell(1)
                        start = False
                elif event.button == 1 and cord[0]:
                    b.grid[cord[1]][cord[2]].mark_cell(0)
                    x, y = pygame.mouse.get_pos()
                    cord = b.collide_point(x, y)
                    if cord[0]:
                        b.grid[cord[1]][cord[2]].mark_cell(1)
                        start = False
                if event.button == 3 and end:
                    x, y = pygame.mouse.get_pos()
                    cord2 = b.collide_point(x, y)
                    if cord2[0] and cord2[1] is not None:
                        b.grid[cord2[1]][cord2[2]].mark_cell(-1)
                        end = False
                elif event.button == 3 and cord2[0]:
                    b.grid[cord2[1]][cord2[2]].mark_cell(0)
                    x, y = pygame.mouse.get_pos()
                    cord2 = b.collide_point(x, y)
                    if cord2[0]:
                        b.grid[cord2[1]][cord2[2]].mark_cell(-1)
                        end = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                dragging_for_walls = True
                if event.button == 2: dragging = True
            elif event.type == pygame.MOUSEBUTTONUP:
                dragging_for_walls = False
                dragging = False
            elif dragging_for_walls and placing:
                mous_pos = pygame.mouse.get_pos()
                yes, row_num, col_num = b.collide_point(*mous_pos)
                if yes and event.buttons[0] == 1:
                    b.grid[row_num][col_num].mark_cell(-2)
                elif yes and event.buttons[2] == 1:
                    b.grid[row_num][col_num].mark_cell(0)
                pygame.time.delay(3)
        pygame.display.set_caption("Pathfinding... - FPS: %.0f" % clock.get_fps())
        clock.tick(FPS)


if __name__ == '__main__':
    main()
