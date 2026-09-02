import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from hsf_engine import crear_logger_video, cerrar_logger_video, _pipeline_video_automatico, _subir_ultimo_resultado_a_drive

logger, ruta_log = crear_logger_video()
try:
    logger.info("Publicacion automatica (GitHub Actions): arrancando.")
    _pipeline_video_automatico(logger, ruta_log)
    _subir_ultimo_resultado_a_drive(logger)
    logger.info("Publicacion automatica (GitHub Actions): terminada OK.")
finally:
    cerrar_logger_video(logger)
