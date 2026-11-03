# Production-Ready Component Set

*Author: AN · Discipline: design-systems · Tags: react, typescript, accessibility*

## ROLE

You are a senior React + TypeScript design systems engineer.

## TASK

Build a production-ready Avatar component set from the attached Figma:
- 5 sizes: xs, sm, md, lg, xl
- 3 variants: neutral, brand, image
- optional bottom-right overlapping badge
- initials support
- image fallback support
- token-driven styling

## CONTEXT

The design shows a circular avatar primitive with:
- neutral: light bg + dark initials
- brand: light bg + dark green initials
- image: cropped circular photo
- optional EU-style badge: blue circle, yellow stars, ring separator

Suggested token mapping:
- bg neutral = gray.100 `#F6F7F4`
- text neutral = gray.900 `#0B0C0A`
- text brand = forestGreen.600 `#163300`
- outline = gray.300 `#D7D8D2`
- badge stars = yellow.500 `#FFD400` :contentReference[oaicite:14]{index=14}

## CONSTRAINTS

- React + TypeScript
- Use `variant`, not `style`, in code API
- Ref-forwarding
- Centralized size config
- Circular only
- `object-fit: cover` for images
- Badge scales by size and overlaps bottom-right
- Good a11y defaults
- No magic numbers scattered through component
- Non-interactive by default

Use:
```ts
type AvatarProps = {
  size?: "xs" | "sm" | "md" | "lg" | "xl";
  variant?: "neutral" | "brand" | "image";
  initials?: string;
  src?: string;
  alt?: string;
  showBadge?: boolean;
  badgeAriaLabel?: string;
  className?: string;
};

## FORMAT

- Avatar.tsx - avatar.styles.ts (or token config) - Badge implementation (inline or separate) - Brief explanation of key decisions - Production-ready - Token-driven - Clean API - Visually accurate to design - Accessible
