from logger.logger import get_logger


logger = get_logger()


def main():
    logger.info("start = main()")
    # do something 
    logger.error("oops! something wrong!!")
    # do something 
    logger.info("end = main()")


if __name__ == "__main__":
    main()
