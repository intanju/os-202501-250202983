def print_table_header(title):
    print(title)
    print("Page   F1   F2   F3   Status")
    print("-" * 30)


def fifo_page_replacement(pages, frame_size):
    frames = []
    page_faults = 0

    print_table_header("FIFO Page Replacement")

    for page in pages:
        if page in frames:
            status = "HIT"
        else:
            status = "FAULT"
            page_faults += 1
            if len(frames) < frame_size:
                frames.append(page)
            else:
                frames.pop(0)
                frames.append(page)

        display = frames + ["-"] * (frame_size - len(frames))
        print(f"{page:<6}{display[0]:<5}{display[1]:<5}{display[2]:<5}{status}")

    print(f"\nTotal Page Fault FIFO: {page_faults}\n")
    return page_faults


def lru_page_replacement(pages, frame_size):
    frames = []
    recent_use = {}
    page_faults = 0

    print_table_header("LRU Page Replacement")

    for i, page in enumerate(pages):
        if page in frames:
            status = "HIT"
        else:
            status = "FAULT"
            page_faults += 1
            if len(frames) < frame_size:
                frames.append(page)
            else:
                lru_page = min(recent_use, key=recent_use.get)
                frames.remove(lru_page)
                del recent_use[lru_page]
                frames.append(page)

        recent_use[page] = i

        display = frames + ["-"] * (frame_size - len(frames))
        print(f"{page:<6}{display[0]:<5}{display[1]:<5}{display[2]:<5}{status}")

    print(f"\nTotal Page Fault LRU: {page_faults}")
    return page_faults


if __name__ == "__main__":
    pages = [1, 3, 0, 3, 5, 6, 3, 1, 6, 2]
    frame_size = 3

    fifo_page_replacement(pages, frame_size)
    lru_page_replacement(pages, frame_size)
