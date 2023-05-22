import Link from "next/link";

export default function MenuUsuario() {
  return (
    <div>
      <Link href="/ajustes">Ajustes</Link>
      <Link href="/ordenes">Ordenes</Link>
      <Link href="/login">Sign Out</Link>
    </div>
  );
}
