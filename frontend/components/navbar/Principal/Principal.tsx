import Link from "next/link";
import MenuUsuario from "./MenuUsuario";

export default function Principal() {
  return (
    <div>
      <Link href="/carritos">Carritos</Link>
      <MenuUsuario />
    </div>
  );
}
