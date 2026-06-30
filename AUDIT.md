# Project Audit Prompts

A set of three comprehensive audit prompts for use with an AI IDE / coding assistant. Run them independently, ideally in this order: **Security → Performance & Bandwidth → Cache**.

---

## 1. Audit Security

**Use this prompt:**

Task: Perform a comprehensive security audit of the existing project and implement security best practices without breaking existing functionality.

### Objectives

1. Audit the entire application (frontend, backend, APIs, database, deployment, and infrastructure) to identify security vulnerabilities and misconfigurations.
2. Check for common security issues, including but not limited to:
   * Authentication vulnerabilities
   * Authorization (RBAC/permission) issues
   * Broken access control
   * Insecure direct object references (IDOR)
   * SQL Injection
   * NoSQL Injection
   * Cross-Site Scripting (XSS)
   * Cross-Site Request Forgery (CSRF)
   * Server-Side Request Forgery (SSRF)
   * Command Injection
   * Path Traversal
   * File upload vulnerabilities
   * Open Redirects
   * Clickjacking
   * CORS misconfiguration
   * Sensitive information exposure
   * Weak password policies
   * Session fixation
   * Session hijacking
   * Insecure cookies
   * Missing HTTPS enforcement
   * Missing security headers
   * Rate limiting issues
   * Brute-force attack protection
   * API security weaknesses
   * Dependency vulnerabilities
   * Secrets or API keys committed into the repository
   * Insecure environment variable handling
   * Logging of sensitive information
3. Review authentication and session management:
   * Secure JWT/session implementation.
   * Validate token expiration and refresh flow.
   * Secure cookie configuration (HttpOnly, Secure, SameSite).
   * Prevent unauthorized access to protected routes.
   * Ensure proper logout invalidates sessions/tokens.
4. Secure all API endpoints:
   * Validate and sanitize every input.
   * Apply server-side validation even if frontend validation exists.
   * Implement proper authorization checks.
   * Prevent mass assignment vulnerabilities.
   * Return generic error messages that do not expose internal implementation.
5. Secure the frontend:
   * Prevent XSS by properly escaping user input.
   * Sanitize HTML rendering.
   * Avoid storing sensitive tokens in localStorage when more secure alternatives are available.
   * Ensure forms include CSRF protection where applicable.
   * Prevent exposure of secrets in client-side code.
6. Improve HTTP and browser security:
   * Add appropriate security headers:
     * Content-Security-Policy (CSP)
     * Strict-Transport-Security (HSTS)
     * X-Content-Type-Options
     * X-Frame-Options
     * Referrer-Policy
     * Permissions-Policy
   * Configure secure CORS rules.
   * Enforce HTTPS in production.
7. Improve deployment and infrastructure security:
   * Ensure production environment variables are secure.
   * Remove debug mode in production.
   * Prevent directory listing.
   * Disable unnecessary server information.
   * Secure file permissions.
   * Protect sensitive configuration files.
   * Review Docker/container security if applicable.
   * Review reverse proxy (Nginx/Apache) configuration if applicable.
8. Review dependencies:
   * Identify vulnerable packages.
   * Upgrade dependencies where safe.
   * Remove unused dependencies.
   * Ensure dependency versions are actively maintained.
9. Protect against abuse:
   * Implement rate limiting on authentication and sensitive endpoints.
   * Prevent brute-force attacks.
   * Prevent abuse of public APIs.
   * Add request validation and size limits where appropriate.
10. Secure file uploads (if applicable):
    * Validate MIME types and file extensions.
    * Enforce file size limits.
    * Prevent executable file uploads.
    * Store uploads securely.
    * Generate random filenames.
11. Review database security:
    * Ensure parameterized queries or ORM protections are used.
    * Validate database permissions follow the principle of least privilege.
    * Prevent information leakage in database errors.
12. Review logging and monitoring:
    * Remove sensitive information from logs.
    * Log security-related events appropriately.
    * Ensure production logs do not expose secrets.
13. Follow security best practices:
    * Apply the principle of least privilege.
    * Use secure defaults.
    * Follow the OWASP Top 10 recommendations.
    * Maintain existing functionality and user experience unless a change is required for security.
14. After implementing improvements, provide:
    * A complete list of vulnerabilities found.
    * Risk level (Critical, High, Medium, Low) for each issue.
    * Files modified.
    * Exact changes made.
    * Rationale for each change.
    * Any remaining recommendations that require architectural or infrastructure changes.

### Important

* Do not remove existing functionality unless it is insecure.
* Prefer secure, production-ready implementations over temporary fixes.
* Preserve application performance where possible.
* Ensure all changes are compatible with the current project architecture and deployment process.
* If a recommended change could affect existing behavior, explain the impact before implementing it.

---

## 2. Audit Performance and Bandwidth Usage

**Use this prompt:**

Task: Perform a comprehensive production performance and bandwidth audit of the existing project to identify why the application is consuming excessive bandwidth in production. Optimize the application to significantly reduce bandwidth usage while maintaining or improving performance and user experience.

### Objectives

1. **Audit the entire production application.** Analyze all factors contributing to high bandwidth usage, including:
   * Frontend assets
   * Backend APIs
   * Database queries
   * Images
   * Videos
   * Fonts
   * JavaScript bundles
   * CSS bundles
   * Third-party libraries
   * External scripts
   * CDN configuration
   * HTTP caching
   * Compression
   * WebSockets/SSE
   * Static assets
   * File downloads/uploads
   * Logging
   * Analytics scripts
   * Monitoring tools
   * Build output
2. **Identify bandwidth bottlenecks.** Find every issue that increases production bandwidth, including but not limited to:
   * Oversized JavaScript bundles
   * Unused JavaScript
   * Unused CSS
   * Duplicate dependencies
   * Duplicate API requests
   * Excessive polling
   * Large API payloads
   * Overfetching data
   * Missing pagination
   * Missing lazy loading
   * Missing code splitting
   * Missing tree shaking
   * Missing image optimization
   * Missing font optimization
   * Uncompressed assets
   * Missing Brotli/Gzip compression
   * Excessive re-rendering
   * Repeated downloads of identical assets
   * Missing browser cache strategy
   * Missing CDN caching
   * Inefficient Service Worker caching
   * Large source maps exposed in production
   * Shipping development-only code to production
   * Large third-party libraries
   * Unnecessary network requests
   * Inefficient GraphQL or REST responses
   * Repeated authentication requests
   * Background requests that can be eliminated
   * Memory leaks causing repeated requests
   * Network waterfalls
3. **Optimize frontend performance.** Implement production-ready optimizations, including:
   * Route-based code splitting
   * Dynamic imports
   * Tree shaking
   * Bundle optimization
   * Remove unused packages
   * Remove dead code
   * Lazy load components
   * Lazy load images
   * Responsive image loading
   * Convert images to WebP or AVIF where appropriate
   * Optimize SVGs
   * Font subsetting
   * Font preloading
   * Minify HTML, CSS, and JavaScript
   * Enable Brotli compression
   * Enable Gzip fallback
   * Preload only critical assets
   * Defer non-critical JavaScript
   * Reduce render-blocking resources
   * Optimize hydration (if SSR is used)
4. **Optimize backend and API usage.** Review every API endpoint and optimize:
   * Response payload size
   * Database queries
   * Serialization
   * Compression
   * Pagination
   * Filtering
   * Caching
   * Query efficiency
   * Eliminate duplicate requests
   * Batch requests where possible
   * Prevent unnecessary polling
   * Optimize WebSocket traffic
   * Reduce repetitive authentication calls
5. **Optimize static assets.** Review images, videos, PDFs, documents, fonts, icons, and static files. Ensure:
   * Proper compression
   * Proper caching
   * Versioned assets
   * CDN optimization
   * Modern image formats
   * Appropriate file sizes
6. **Optimize production build.** Review the production build configuration and ensure:
   * Production mode is enabled
   * Development code is removed
   * Source maps are disabled (unless explicitly required)
   * Bundles are minimized
   * Assets are fingerprinted/versioned
   * Duplicate chunks are eliminated
   * Vendor bundles are optimized
7. **Optimize caching without serving stale content.** Ensure:
   * Browser caching is configured correctly
   * CDN cache is optimized
   * Cache invalidation occurs automatically on every deployment
   * Service Worker does not serve outdated assets
   * Hashed assets are used
   * HTML always references the latest build assets
8. **Analyze third-party dependencies.** Identify heavy libraries, duplicate libraries, unused packages, expensive analytics, slow SDKs, and third-party scripts consuming excessive bandwidth. Replace or remove them where appropriate.
9. **Measure performance before and after optimization.** Compare key metrics such as:
   * Total page size
   * JavaScript bundle size
   * CSS bundle size
   * Image payload
   * Font payload
   * API payload size
   * Initial page load size
   * Number of HTTP requests
   * Largest Contentful Paint (LCP)
   * First Contentful Paint (FCP)
   * Total Blocking Time (TBT)
   * Time to Interactive (TTI)
   * Cumulative Layout Shift (CLS)
   * Average bandwidth consumed per page load
   * Estimated monthly bandwidth usage
10. **Validate production behavior.** Verify that:
    * No functionality is broken.
    * Performance is maintained or improved.
    * Assets are correctly cached.
    * Users always receive the latest deployment.
    * Bandwidth usage is significantly reduced.
    * APIs return only the required data.
    * There are no unnecessary background network requests.
11. **Deliver a comprehensive report**, including:
    * **Executive Summary** — overall findings, main causes of excessive bandwidth usage, overall improvements achieved.
    * **Bandwidth Analysis** — estimated bandwidth usage before/after optimization, percentage reduction, largest bandwidth consumers.
    * **Performance Analysis** — before vs. after metrics, bundle size comparison, asset size comparison, API payload comparison, number of network requests before vs. after, load time improvements.
    * **Changes Implemented** — files modified, optimizations applied, rationale for each change.
    * **Remaining Recommendations** — additional improvements that require infrastructure changes, CDN recommendations, database optimization opportunities, long-term scalability recommendations.

### Important Requirements

* Do not sacrifice functionality to reduce bandwidth.
* Preserve or improve user experience.
* Follow production-ready and industry best practices.
* Prioritize sustainable optimizations over temporary fixes.
* If any optimization could affect existing behavior, explain the impact before implementing it.
* Aim to minimize bandwidth consumption while maintaining fast load times, scalability, and reliability in production.

---

## 3. Audit Cache

**Use this prompt:**

Task: Audit the existing project to identify all caching mechanisms that may cause users to receive outdated content after a production deployment.

### Objectives

1. Identify every caching layer used in the project, including but not limited to:
   * Browser cache
   * Service Worker (PWA)
   * HTTP Cache-Control headers
   * CDN caching (Cloudflare, AWS CloudFront, Vercel, Netlify, etc.)
   * Reverse proxy cache (Nginx, Apache, etc.)
   * Application-level cache
   * API response cache
   * Build asset caching (JS/CSS/images)
   * Framework-specific caching (Next.js, Nuxt, Laravel, React, Vue, etc.)
   * Redis or other server-side cache
2. Explain for each cache mechanism:
   * Where it is configured.
   * Why it exists.
   * Whether it can cause users to see stale content after deployment.
3. If any cache mechanism exists, modify the project so that every production deployment automatically serves the latest version of the application without requiring users to manually clear their browser cache.
4. Implement deployment-safe cache invalidation using best practices:
   * Use hashed/versioned filenames for static assets.
   * Invalidate old caches on every production build.
   * Ensure HTML always references the newest asset versions.
   * Configure proper Cache-Control headers.
   * If a Service Worker exists, ensure it immediately activates the new version (`skipWaiting` and `clientsClaim` where appropriate) and removes outdated caches.
   * Delete old cache storage during activation.
   * Ensure API responses are not unintentionally cached unless explicitly intended.
   * If a CDN is used, configure automatic cache purge or versioning during deployment.
5. Verify that after a fresh production deployment:
   * Users automatically receive the latest frontend without a hard refresh.
   * Old JS/CSS bundles are never reused after deployment.
   * No stale Service Worker remains active.
   * New API changes are immediately reflected.
   * Existing performance optimizations are preserved where possible.
6. At the end, provide:
   * A list of all caching mechanisms found.
   * The files that were modified.
   * The exact changes made.
   * The reason for each change.
   * Any remaining recommendations to improve cache invalidation and deployment reliability.

### Important

Do not disable caching entirely. Keep performance optimizations while ensuring that each production deployment automatically invalidates outdated caches and serves the newest application version to all users. Use industry best practices for cache busting and cache invalidation.