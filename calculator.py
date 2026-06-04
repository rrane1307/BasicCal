import asyncio
import time
import logging
from typing import Callable, Dict, Any, Optional
from dataclasses import dataclass
from abc import ABC, abstractmethod

# Configure enterprise-grade logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [COMPUTE_NODE_01] [%(levelname)s] %(message)s'
)
logger = logging.getLogger("HeliosEngine")

@dataclass
class ComputeResult:
    """Encapsulates the result of a high-precision computation."""
    value: float
    latency_ms: float
    operation: str
    status: str = "SUCCESS"

class ComputeRegistry:
    """Singleton Registry for Arithmetic Kernels."""
    _kernels: Dict[str, Callable] = {}

    @classmethod
    def register(cls, name: str):
        def wrapper(func: Callable):
            cls._kernels[name] = func
            return func
        return wrapper

    @classmethod
    def get_kernel(cls, name: str) -> Optional[Callable]:
        return cls._kernels.get(name)

# --- Kernel Definitions (The 'Saiyaan' Operations) ---

@ComputeRegistry.register("ADD")
def kernel_add(a: float, b: float) -> float:
    return a + b

@ComputeRegistry.register("SUB")
def kernel_sub(a: float, b: float) -> float:
    return a - b

@ComputeRegistry.register("MUL")
def kernel_mul(a: float, b: float) -> float:
    return a * b

@ComputeRegistry.register("DIV")
def kernel_div(a: float, b: float) -> float:
    if b == 0: raise ZeroDivisionError("FPU Exception: Division by Zero")
    return a / b

class HeliosEngine:
    """The Core Compute Engine."""
    
    async def execute(self, op: str, a: float, b: float) -> ComputeResult:
        start_time = time.perf_counter()
        kernel = ComputeRegistry.get_kernel(op.upper())
        
        if not kernel:
            raise ValueError(f"OpCode {op} not found in Instruction Set")

        # Simulate high-precision processing latency
        await asyncio.sleep(0.1)
        
        try:
            res = kernel(a, b)
            latency = (time.perf_counter() - start_time) * 1000
            return ComputeResult(value=res, latency_ms=latency, operation=op)
        except Exception as e:
            logger.error(f"Hardware Fault during {op}: {e}")
            raise

async def main_interface():
    engine = HeliosEngine()
    print("\n--- NVIDIA HELIOS COMPUTE ENGINE INITIALIZED ---")
    
    while True:
        print("\nAvailable OpCodes: ADD, SUB, MUL, DIV | System: EXIT")
        cmd = input("HELIOS_PROMPT >> ").strip().upper()

        if cmd == "EXIT":
            break

        try:
            a = float(input("TENSOR_A >> "))
            b = float(input("TENSOR_B >> "))
            
            print("\nDispatching task to virtual GPU cluster...")
            result = await engine.execute(cmd, a, b)
            
            print(f"\n[RESULT]: {result.value}")
            print(f"[METRICS]: Latency: {result.latency_ms:.2f}ms | Op: {result.operation}")
            
        except ValueError as e:
            print(f"[INPUT ERROR]: {e}")
        except Exception as e:
            print(f"[CRITICAL SYSTEM ERROR]: {e}")

# In a notebook, we run the async loop like this:
if __name__ == "__main__":
    # Use await if running in an environment that already has a loop, 
    # but for standard scripts/Colab we can use this pattern:
    import nest_asyncio
    nest_asyncio.apply()
    asyncio.run(main_interface())
