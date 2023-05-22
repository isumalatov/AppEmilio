"use client";

import Principal from "./Principal/Principal";
import Categorias from "./Categorias";
import { usePathname } from "next/navigation";

export default function Navbar() {
  const pathname = usePathname();

  const isHomePage = pathname === "/";
  const isShoesPage = pathname === "/zapatos";
  const isAccessoriesPage = pathname === "/accesorios";
  const isLoginPage = pathname === "/login";
  const isSignUpPage = pathname === "/accesorios";

  return (
    <div>
      {isLoginPage || isSignUpPage ? null : (
        <div>
          <Principal />
          {isHomePage || isShoesPage || isAccessoriesPage ? (
            <Categorias />
          ) : null}
        </div>
      )}
    </div>
  );
}
