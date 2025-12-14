import uvicorn
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))

from src import create_app
from src.core.config import settings




app = create_app()


if __name__ == "__main__":
    uvicorn.run(
        app="src.main:app",
        host=settings.uv.host,
        port=settings.uv.port,
        reload=settings.uv.reload
    )